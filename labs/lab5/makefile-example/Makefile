all: dynamic_block static_block
clean:
	rm *.o *.so dynamic_block
dynamic_block: program.o libshared.so
	cc program.o libshared.so -o dynamic_block -Wl,-rpath .
static_block: program.o libstatic.a
	cc program.o libstatic.a -o static_block -Wl,-rpath .
program.o: program.c
	cc -c program.c -o.program.o
libshared.so: block.o 
	cc -shared -o libshared.so block.o 
libstatic.a: block.o 
	ar qc libstatic.a block.o 
block.o: source/block.c
	cc -fPIC -c source/block.c -o block.o
program.o: headers/block.h
block.o: headers/block.h