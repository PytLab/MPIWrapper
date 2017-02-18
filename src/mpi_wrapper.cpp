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
bool MPIWrapper::finalized()
{
    return MPI::Is_finalized();
}


// -----------------------------------------------------------------------------
//
bool MPIWrapper::initialized()
{
    return MPI::Is_initialized();
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


// -----------------------------------------------------------------------------
//
int MPIWrapper::rank(const MPI::Intracomm & comm)
{
    int rank;
    rank = comm.Get_rank();
    return rank;
}


// -----------------------------------------------------------------------------
//
int MPIWrapper::size(const MPI::Intracomm & comm)
{
    int size;
    size = comm.Get_size();
    return size;
}


// -----------------------------------------------------------------------------
//
void MPIWrapper::barrier(const MPI::Intracomm & comm)
{
    comm.Barrier();
}

