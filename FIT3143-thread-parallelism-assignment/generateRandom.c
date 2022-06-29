#include "wsn.h"

int generateRandom(MPI_Comm *newComm, int *rank, int *events, int *size, struct Details *details, struct Msg *msg, char key[73]) {
    MPI_Status statuses[TRANS];
    MPI_Request requests[TRANS];

    char cn;
    int source, dest, n;
    int i = 0, j = 0;
    char recvd[EL] = {[0 ... EL-1] = -1};
    int adj[EL] = {[0 ... EL-1] = -1};
    int count[MAX] = {};

    (*details).msgNum = 0;

    srandom(time(NULL)+random() | *rank);
    n = random() % MAX;
    cn = n + '0';
    cn = encCalculation(&cn, key);

    //node below
    MPI_Cart_shift(*newComm, 0, 1, &source, &dest);
    if (dest > -1) {
        MPI_Isend(&cn, 1, MPI_CHAR, dest, 0, *newComm, &requests[i++]);
        (*details).msgNum++;
    }

    if (source > -1) {
        MPI_Irecv(&recvd[j++], 1, MPI_CHAR, source, 0, *newComm, &requests[i++]);
        adj[j-1] = source;
    }

    // node above
    MPI_Cart_shift(*newComm, 0, -1, &source, &dest);
    if (dest > -1) {
        MPI_Isend(&cn, 1, MPI_CHAR, dest, 0, *newComm, &requests[i++]);
        (*details).msgNum++;
    }

    if (source > -1) {
        MPI_Irecv(&recvd[j++], 1, MPI_CHAR, source, 0, *newComm, &requests[i++]);
        adj[j-1] = source;
    }

    //right node
    MPI_Cart_shift(*newComm, 1, 1, &source, &dest);
    if (dest > -1) {
        MPI_Isend(&cn, 1, MPI_CHAR, dest, 0, *newComm, &requests[i++]);
        (*details).msgNum++;
    }

    if (source > -1) {
        MPI_Irecv(&recvd[j++], 1, MPI_CHAR, source, 0, *newComm, &requests[i++]);
        adj[j-1] = source;
    }

    //left node
    MPI_Cart_shift(*newComm, 1, -1, &source, &dest);
    if (dest > -1) {
        MPI_Isend(&cn, 1, MPI_CHAR, dest, 0, *newComm, &requests[i++]);
        (*details).msgNum++;
    }

    if (source > -1) {
        MPI_Irecv(&recvd[j++], 1, MPI_CHAR, source, 0, *newComm, &requests[i++]);
        adj[j-1] = source;
    }

    MPI_Waitall(i, requests, statuses);

    for (i = 0; i < EL; i++) {
        if (recvd[i] < -1) {
            recvd[i] = decCalculation(&recvd[i], key);
        }
    }

    if (j >= 3) {
        int k, m = 0;
        time_t t;
        for (k = 0; k < EL; k++) {
            if (recvd[k] > -1) {
                count[recvd[k] - '0']++;
            }
        }
        
        for (k = 0; k < MAX; k++) {
            if (count[k] >= 3) {
                *events += 1;
                (*details).num = k;
                time(&t);
                strftime((*details).timestamp, sizeof((*details).timestamp), "%H:%M:%S", localtime(&t));
                break;
            }
        }

        if (*events > 0) {
            for(k = 0; k < EL; k++) {
                if (recvd[k] - '0' == (*details).num) {
                    (*details).adjNodes[m++] = adj[k];
                }
            }

            (*details).msgNum++;
            
		    encrypt_openmp(details, msg, &m, key);
		    MPI_Send(&(*msg), sizeof(*msg), MPI_BYTE, *size - 1, 0, MPI_COMM_WORLD);
        }
    }

    return(0);
}
