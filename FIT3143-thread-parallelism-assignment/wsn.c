#include "wsn.h"

//Main program
int main(int argc, char** argv) 
{   
    /* MPI properties */
    int size, rank;
    MPI_Comm newComm;
    MPI_Status stat;

    MPI_Init(&argc, &argv);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    
    /* struct properties */
    struct Details details;
    int d_blockLengths[4] = {1, 10, 4, 1};
    MPI_Datatype d_mpiStruct;
    MPI_Aint d_indices[4];
    MPI_Datatype d_baseTypes[4] = {MPI_INT, MPI_CHAR, MPI_INT, MPI_INT};

    MPI_Address(&details.num, &d_indices[0]);
    MPI_Address(&details.timestamp, &d_indices[1]);
    MPI_Address(&details.adjNodes, &d_indices[2]);
    MPI_Address(&details.msgNum, &d_indices[3]);

    d_indices[3] = d_indices[3] - d_indices[0];
    d_indices[2] = d_indices[2] - d_indices[0];
    d_indices[1] = d_indices[1] - d_indices[0];
    d_indices[0] = 0;

    MPI_Type_struct(4, d_blockLengths, d_indices, d_baseTypes, &d_mpiStruct);
    MPI_Type_commit(&d_mpiStruct);

    /* struct properties */
    struct Msg msg;
    int m_blockLengths[3] = {73, 31, 1};
    MPI_Datatype m_mpiStruct;
    MPI_Aint m_indices[3];
    MPI_Datatype m_baseTypes[3] = {[0 ... 1] = MPI_CHAR, MPI_DOUBLE};

    MPI_Address(&msg.ciphertext, &m_indices[0]);
    MPI_Address(&msg.et_ciphertext, &m_indices[1]);
    MPI_Address(&msg.et_ciphertext, &m_indices[2]);

    m_indices[1] = m_indices[2] - m_indices[0];
    m_indices[1] = m_indices[1] - m_indices[0];
    m_indices[0] = 0;

    MPI_Type_struct(3, m_blockLengths, m_indices, m_baseTypes, &m_mpiStruct);
    MPI_Type_commit(&m_mpiStruct);

    int iteration = ITERATION;
    int width, height, i, total, events, eventsTriggered, msgPassed;
    int dim[DIM], period[DIM];
    char key[73] = {'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l'};

    FILE * file;

    // to calculate average communication time
    // please uncomment to verify
    // please uncomment calculate speedup in the next if condition as well
    // if (rank == size - 1) {
    //     file = fopen("commtime.txt", "w+");
    //     MPI_Status stat;
    //     double start;
    //     double sum;
    //     int iteration = ITERATION;

    //     while (iteration > 0) {
    //         MPI_Recv(&start, 1, MPI_DOUBLE, 0, 0, MPI_COMM_WORLD, &stat);
    //         double time = MPI_Wtime() - start;
    //         sum += time;
    //         fprintf(file, "communication time = %lf\n", time);
    //         iteration -= 1;
    //     }

    //     fprintf(file, "average communication time = %lf", sum/ITERATION);
    //     fclose(file);
    // }

    if (rank == 0) {
	// to calculate average speedup
	// please uncomment to verify
    // calculateSpeedUp(&size);

        printf("\nEnter width: \n");
        fflush(stdout);
        scanf("%d", &width);

        printf("\nEnter height: \n");
        fflush(stdout);
        scanf("%d", &height);

        if (width * height != size - 1) {
            MPI_Abort(MPI_COMM_WORLD, 1);
            return(0);
        } 
    }

    MPI_Bcast(&width, 1, MPI_INT, 0, MPI_COMM_WORLD);
    MPI_Bcast(&height, 1, MPI_INT, 0, MPI_COMM_WORLD);

    dim[0] = width;
    dim[1] = height;
    period[0] = period[1] = 0;

    MPI_Dims_create(size - 1, DIM, dim);
    MPI_Cart_create(MPI_COMM_WORLD, DIM, dim, period, 0, &newComm);
	
	if(rank == size - 1) {
		 file = fopen("log.txt", "w+");
	}

    while (iteration > 0) {
        events = 0;
        if (newComm != MPI_COMM_NULL) {
            generateRandom(&newComm, &rank, &events, &size, &details, &msg, key);
        }

        MPI_Reduce(&events, &eventsTriggered, 1, MPI_INT, MPI_SUM, size - 1, MPI_COMM_WORLD);

        if (rank == size - 1) {
            total += eventsTriggered;
            while (eventsTriggered > 0) {
                MPI_Recv(&msg, sizeof(msg), MPI_BYTE, MPI_ANY_SOURCE, 0, MPI_COMM_WORLD, &stat);
                double end = MPI_Wtime();
                decrypt(&msg, key);
                // printf("%s\n", msg.ciphertext);
                for (i = 0; i < 73; i++) {
                   if (msg.ciphertext[i] != ';') {
                       fputc(msg.ciphertext[i], file);
                    } else {
                       fprintf(file, ", reference node: %d\n", stat.MPI_SOURCE);
                       msgPassed += (msg.ciphertext[i+2] - '0');
                       fprintf(file, "communication time: %lf\n", end - msg.start);
                       break;
                    }
                }

                for (i = 0; i < 30; i++) {
                   if (msg.et_ciphertext[i] != ';') {
                       fputc(msg.et_ciphertext[i], file);
                   } else {
                       fputs("\n\n", file);
                       break;
                   }
                }
                eventsTriggered -= 1;
            }
        }
	    iteration -= 1;
        sleep(0.05);
    }

	if (rank == size - 1) {
        fprintf(file, "total events in the network: %d\n", total);
        fprintf(file, "total messages passed in the network: %d", msgPassed);
		fclose(file);
	}

    MPI_Finalize();
    return(0);
}