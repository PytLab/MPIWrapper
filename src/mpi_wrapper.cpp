/*! \file  mpi_wrapper.cpp
 *  \brief File for the implementation code of the wrapper for MPI routines.
 *
 *  \author ShaoZhengjiang
 *  \contact shaozhengjiang@gmail.com
 */


#include "mpi_wrapper.h"


// -----------------------------------------------------------------------------
//
void MPIWrapper::init()
{
    // Initialization check.
    if (initialized())
    {
        return;
    }

    // Make the init call.
    MPI::Init();
}


// -----------------------------------------------------------------------------
//
void MPIWrapper::finalize()
{
    if (finalized())
    {
        return;
    }

    MPI::Finalize();
}

