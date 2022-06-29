#include "wsn.h"

int encCalculation(char *c, char *k) {
    if (*c >= 'a' && *c <= 'z') {
        *c = ((*c - 'a') + (*k - 'a')) % 26;
    } else if (*c >= 48 && *c <= 57) {
        *c = *c - *c - *c - MAX;
    }
    return *c;
}

/*Vignere cipher encryption*/
int encrypt_serial(struct Details *details, struct Msg *msg, int *adjCount, char key[73]) {
    int i, j;
    
    if (*adjCount == 3) {
        sprintf((*msg).ciphertext, "timestamp: %s, random number: %d, adjacent nodes: %d, %d, %d; %d", (*details).timestamp, (*details).num, (*details).adjNodes[0], (*details).adjNodes[1], (*details).adjNodes[2], (*details).msgNum);
    } else {
        sprintf((*msg).ciphertext, "timestamp: %s, random number: %d, adjacent nodes: %d, %d, %d, %d; %d", (*details).timestamp, (*details).num, (*details).adjNodes[0], (*details).adjNodes[1], (*details).adjNodes[2], (*details).adjNodes[3], (*details).msgNum);
    }
    
    double start = MPI_Wtime();
    for (i = 0; i < 73; i++) {
    	for (j = 0; j < ENC_ITERATION; j++) {
            (*msg).ciphertext[i] = encCalculation(&msg->ciphertext[i], &key[i]);
            sleep(0.05);
        }
    }
    double end = MPI_Wtime();

    sprintf((*msg).et_ciphertext, "encryption time: %lf;", end - start);

    for (i = 0; i < 31; i++) {
    	for (j = 0; j < ENC_ITERATION; j++) {
    	    (*msg).et_ciphertext[i] = encCalculation(&msg->et_ciphertext[i], &key[i]);
		    sleep(0.05);
    	}
    }

    (*msg).start = MPI_Wtime();
    return(0);
}

int encrypt_openmp(struct Details *details, struct Msg *msg, int *adjCount, char key[73]) {
    int i, j;
    int chunk = 73/NUM_THREADS;

    if (*adjCount == 3) {
        sprintf((*msg).ciphertext, "timestamp: %s, random number: %d, adjacent nodes: %d, %d, %d; %d", (*details).timestamp, (*details).num, (*details).adjNodes[0], (*details).adjNodes[1], (*details).adjNodes[2], (*details).msgNum);
    } else {
        sprintf((*msg).ciphertext, "timestamp: %s, random number: %d, adjacent nodes: %d, %d, %d, %d; %d", (*details).timestamp, (*details).num, (*details).adjNodes[0], (*details).adjNodes[1], (*details).adjNodes[2], (*details).adjNodes[3], (*details).msgNum);
    }

    // to obtain screenshot before encryption
    // printf("%s\n", (*msg).ciphertext);

	/* Initialization */
    omp_set_num_threads(NUM_THREADS);
    double start = MPI_Wtime();
    #pragma omp parallel private(i)
    { 
        #pragma omp for schedule(static, chunk) collapse(2)
        for (i = 0; i < 73; i++) {
        	for (j = 0; j < ENC_ITERATION; j++) {
                (*msg).ciphertext[i] = encCalculation(&msg->ciphertext[i], &key[i]);
                sleep(0.05);
            }
        }
    }
	double end = MPI_Wtime();	
	
    // to obtain screenshot after encryption
    // printf("%s\n", (*msg).ciphertext);

    sprintf((*msg).et_ciphertext, "encryption time: %lf;", end - start);

    for (i = 0; i < 31; i++) {
    	for (j = 0; j < ENC_ITERATION; j++) {
    	    (*msg).et_ciphertext[i] = encCalculation(&msg->et_ciphertext[i], &key[i]);
    	}
    }

    (*msg).start = MPI_Wtime();
    return(0);
}
