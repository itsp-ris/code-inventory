#include "wsn.h"

// obtain average speed up
int calculateSpeedUp(int *size) {
    struct Msg msg;
    struct Details details;
    char key[73] = {'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l', 'e', 'g', 'l'};
    int iteration = ITERATION;
    int el = EL;
    double sum = 0;

    FILE * file;
    time_t t;

    details.num = 2;
    time(&t);
    strftime(details.timestamp, sizeof(details.timestamp), "%H:%M:%S", localtime(&t));
    details.adjNodes[0] = 1;
    details.adjNodes[1] = 11;
    details.adjNodes[2] = 5;
    details.adjNodes[3] = 7;
    details.msgNum = 4;
    
    file = fopen("speedup.txt", "w+");

    while (iteration > 0) {
        double startp = MPI_Wtime();
        encrypt_openmp(&details, &msg, &el, key);
        double endp = MPI_Wtime();
        double starts = MPI_Wtime();
        encrypt_serial(&details, &msg, &el, key);
        double ends = MPI_Wtime();
        double commtime = MPI_Wtime();
        MPI_Send(&commtime, 1, MPI_DOUBLE, *size - 1, 0, MPI_COMM_WORLD);
        double speedup = (ends-starts)/(endp-startp);
        sum += speedup;
        fprintf(file, "speedup = %lf\n", speedup);
	iteration -= 1;
    }

    fprintf(file, "average speedup = %lf", sum/ITERATION);
    fclose(file);
    return(0);
}