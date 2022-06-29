#include <stdio.h>
#include <time.h>
#include <unistd.h>
#include <stdlib.h>
#include <omp.h>
#include "mpi.h"


#define DIM 2
#define TRANS 8
#define MAX 4
#define EL 4
#define ITERATION 100
#define ENC_ITERATION 5
#define NUM_THREADS 4

struct Details {
    int num;
    char timestamp[10];
    int adjNodes[4];
    int msgNum;
} details;

struct Msg {
    char ciphertext[73];
    char et_ciphertext[31];
    double start;
} msg;

int calculateSpeedUp(int *size);
int generateRandom(MPI_Comm *newComm, int *rank, int *events, int *size, struct Details *details, struct Msg *msg, char key[73]);
int encCalculation(char *c, char *k);
int encrypt_serial(struct Details *details, struct Msg *msg, int *adjCount, char key[73]);
int encrypt_openmp(struct Details *details, struct Msg *msg, int *adjCount, char key[73]);
int decrypt(struct Msg *msg, char key[73]);
int decCalculation(char *c, char *k);