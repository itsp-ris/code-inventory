ALL: wsn

wsn: wsn.c
	mpicc -Iasgn2 -fopenmp -o wsn wsn.c generateRandom.c encrypt.c decrypt.c calculateSpeedup.c

run:
	mpirun -n 21 wsn

clean:
	/bin/rm -f wsn *.o