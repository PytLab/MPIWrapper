# Makefile for MPI wrapper
# Author: ShaoZhengjiang
# Contact: shaozhengjiang@gmail.com

CXX = mpicxx
SWIG = swig
SWIGFLAGS = -python -c++ -Wall -Werror
CPPFLAGS = -O2 -fPIC -std=c++0x -c -Wall -Werror
INCLUDE = -I/usr/include/python2.7 -I./src -I./

src/mpiwrapper/_mpiwrapper.so: src/mpi_wrapper.o wrap/mpi_wrapper_wrap.o
	$(CXX) -shared $(INCLUDE) $^ -o $@
	cp wrap/mpiwrapper.py src/mpiwrapper

wrap/mpi_wrapper_wrap.o: wrap/mpi_wrapper_wrap.cxx
	$(CXX) $(CPPFLAGS) $(INCLUDE) $^ -o $@

src/mpi_wrapper.o: src/mpi_wrapper.cpp
	$(CXX) $(CPPFLAGS) $(INCLUDE) $^ -o $@

wrap/mpi_wrapper_wrap.cxx: wrap/mpi_wrapper.i
	$(SWIG) $(SWIGFLAGS) $(INCLUDE) $^

clean:
	find . -name "*.so" | xargs rm -rf
	find . -name "*.o" | xargs rm -rf
	find . -name "*.pyc" | xargs rm -rf
	find . -name "*.cxx" | xargs rm -rf
	rm -rf wrap/*.py src/mpiwrapper/mpiwrapper.py

