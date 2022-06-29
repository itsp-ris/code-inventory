#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>

int writeFile(unsigned char* writeArray, int *sz, int *rem, const int *iYmax, const int *iXMax, int *size, int *rank);

//Main program
int main(int argc, char** argv) 
{	
	/* Clock Information */
    double end, start = MPI_Wtime();
    const int iXmax = 8000; // default
	const int iYmax = 8000; // default

    /* color component ( R or G or B) is coded from 0 to 255 */
	/* it is 24 bit color RGB file */
	const int MaxColorComponentValue = 255; 
	FILE * fp;
	char *filename = "Mandelbrot.ppm";
	char *comment = "# ";	/* comment should start with # */

    /* MPI properties */
    int size, rank;
    MPI_Status Stat;

    MPI_Init(&argc, &argv);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        /* create new file,give it a name and open it in binary mode  */
	    fp = fopen(filename, "w"); /* b -  binary mode */

	    /*write ASCII header to the file (PPM file format)*/
	    fprintf(fp,"P6\n %s\n %d\n %d\n %d\n", comment, iXmax, iYmax, MaxColorComponentValue);

	    printf("File: %s successfully opened for writing.\n", filename);
	    printf("Computing Mandelbrot Set. Please wait...\n");
    }

	int p, i;
    int rem = iYmax%size;
    int eppr = (iYmax-rem)/size;
	int sz = eppr*iXmax*3;
    unsigned char *writeArray = (char*) malloc(sz*sizeof(unsigned char));

    writeFile(writeArray, &sz, &rem, &iYmax, &iXmax, &size, &rank);

    if (rank == 0) {
		unsigned char* temp = (char *) malloc((sz*(size - 1))*sizeof(unsigned char));
        for (p = 1; p < size; p++) {
            MPI_Recv(temp + (sz*(p - 1)), sz, MPI_UNSIGNED_CHAR, p, MPI_ANY_TAG, MPI_COMM_WORLD, &Stat);
        }

        for(i = 0; i < sz; i+=(iXmax*3)) {
            fwrite(writeArray + i, sizeof(unsigned char), iXmax*3, fp);
            for (p = 1; p < size; p++) {
                fwrite(temp + i + (sz*(p - 1)), sizeof(unsigned char), iXmax*3, fp);
            }
        }

        if (rem > 0) {
			MPI_Recv(writeArray, sz, MPI_UNSIGNED_CHAR, size - 1, MPI_ANY_TAG, MPI_COMM_WORLD, &Stat);
		}

        int j;

        for (j = 0; j < rem*iXmax*3; j+=(iXmax*3)) {
            fwrite(writeArray + j, sizeof(unsigned char), iXmax*3, fp);
        }

		printf("Completed Computing Mandelbrot Set.\n");
		fclose(fp);
		printf("File: %s successfully closed.\n", filename);
		free(temp);
    }

    free(writeArray);
	MPI_Finalize();
	if (rank == 0) {
		end = MPI_Wtime();
		printf("Mandelbrot computational process time: %lf\n", (end-start));
	}
	return(0);
}

int writeFile(unsigned char* writeArray, int *sz, int *rem, const int *iYmax, const int *iXmax, int *size, int *rank) {
	/* screen ( integer) coordinate */
	int iX, iY;

	/* world ( double) coordinate = parameter plane*/
	double Cx, Cy;
	const double CxMin = -2.5;
	const double CxMax = 1.5;
	const double CyMin = -2.0;
	const double CyMax = 2.0;

	/* */
	double PixelWidth = (CxMax - CxMin)/(*iXmax);
	double PixelHeight = (CyMax - CyMin)/(*iYmax);

	// RGB color array
	static unsigned char color[3];

	/* Z = Zx + Zy*i;	Z0 = 0 */
	double Zx, Zy;
	double Zx2, Zy2; /* Zx2 = Zx*Zx;  Zy2 = Zy*Zy  */
	/*  */
	int Iteration;
	const int IterationMax = 2000; // default

	/* bail-out value , radius of circle ;  */
	const double EscapeRadius = 400;
	double ER2 = EscapeRadius * EscapeRadius;
	
    int i = 0, sp = *rank, ep = *iYmax - (*rem);

	for (iY = sp; iY < ep; iY+=(*size)) {
		Cy = CyMin + (iY * PixelHeight);
		if (fabs(Cy) < (PixelHeight / 2))
		{
			Cy = 0.0; /* Main antenna */
		}

		for(iX = 0; iX < *iXmax; iX++)
		{
			Cx = CxMin + (iX * PixelWidth);
			/* initial value of orbit = critical point Z= 0 */
			Zx = 0.0;
			Zy = 0.0;
			Zx2 = Zx * Zx;
			Zy2 = Zy * Zy;

			/* */
			for(Iteration = 0; Iteration < IterationMax && ((Zx2 + Zy2) < ER2); Iteration++)
			{
				Zy = (2 * Zx * Zy) + Cy;
				Zx = Zx2 - Zy2 + Cx;
				Zx2 = Zx * Zx;
				Zy2 = Zy * Zy;
			};

			/* compute  pixel color (24 bit = 3 bytes) */
			if (Iteration == IterationMax)
			{
				// Point within the set. Mark it as black
				color[0] = 0;
				color[1] = 0;
				color[2] = 0;
			}
			else 
			{
				// Point outside the set. Mark it as white
				double c = 3*log((double)Iteration)/log((double)(IterationMax) - 1.0);
				if (c < 1)
				{
					color[0] = 0;
					color[1] = 0;
					color[2] = 255*c;
				}
				else if (c < 2)
				{
					color[0] = 0;
					color[1] = 255*(c-1);
					color[2] = 255;
				}
				else
				{
					color[0] = 255*(c-2);
					color[1] = 255;
					color[2] = 255;
				}
			}

            /* store color to the array */
            writeArray[i] = color[0];
            writeArray[i + 1] = color[1];
            writeArray[i + 2] = color[2];
            i += 3;
		}
	}

    if (*rank > 0) {
        MPI_Send(writeArray, *sz, MPI_UNSIGNED_CHAR, 0, 0, MPI_COMM_WORLD);
    }

    if (*rem > 0 && *rank == ((*size) - 1)) {
        sp = *iYmax - (*rem);
        i = 0;
        for (iY = sp; iY < *iYmax; iY++) {
		    Cy = CyMin + (iY * PixelHeight);
		    if (fabs(Cy) < (PixelHeight / 2))
		    {
			    Cy = 0.0; /* Main antenna */
		    }

            for(iX = 0; iX < *iXmax; iX++)
            {
                Cx = CxMin + (iX * PixelWidth);
                /* initial value of orbit = critical point Z= 0 */
                Zx = 0.0;
                Zy = 0.0;
                Zx2 = Zx * Zx;
                Zy2 = Zy * Zy;

                /* */
                for(Iteration = 0; Iteration < IterationMax && ((Zx2 + Zy2) < ER2); Iteration++)
                {
                    Zy = (2 * Zx * Zy) + Cy;
                    Zx = Zx2 - Zy2 + Cx;
                    Zx2 = Zx * Zx;
                    Zy2 = Zy * Zy;
                };

                /* compute  pixel color (24 bit = 3 bytes) */
                if (Iteration == IterationMax)
                {
                    // Point within the set. Mark it as black
                    color[0] = 0;
                    color[1] = 0;
                    color[2] = 0;
                }
                else 
                {
                    // Point outside the set. Mark it as white
                    double c = 3*log((double)Iteration)/log((double)(IterationMax) - 1.0);
                    if (c < 1)
                    {
                        color[0] = 0;
                        color[1] = 0;
                        color[2] = 255*c;
                    }
                    else if (c < 2)
                    {
                        color[0] = 0;
                        color[1] = 255*(c-1);
                        color[2] = 255;
                    }
                    else
                    {
                        color[0] = 255*(c-2);
                        color[1] = 255;
                        color[2] = 255;
                    }
                }

                /* store color to the array */
                writeArray[i] = color[0];
                writeArray[i + 1] = color[1];
                writeArray[i + 2] = color[2];
                i += 3;
            }
        }

        MPI_Send(writeArray, *sz, MPI_UNSIGNED_CHAR, 0, 0, MPI_COMM_WORLD);
    }

	return(0);
}
