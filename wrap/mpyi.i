/*! \brief SWIG interface file for MPI wrapping
 *  \author ShaoZhengjiang
 *  \contact shaozhengjiang@gmail.com
 */

%module mpyi

// Include headers in cpp files. 
%{
#include "mpi_wrapper.h"
%}

// Include MPI wrapper definition.
%include "mpi_wrapper.h"

