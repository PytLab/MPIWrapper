/*! \file  mpi_wrapper.h
 *  \brief Intrerfaces of the common MPI routines.
 *
 *  \author ShaoZhengjiang
 *  \contact shaozhengjiang@gmail.com
 */


#ifndef __MPIWRAPPER__
#define __MPIWRAPPER__

#include "mpih.h"

/// Struct for handling MPI functions to be wrapped.
class MPIWrapper {

public:

    /*! \brief Wrapps MPI::Initialize
     */
    static void init();

    /*! \brief Wrap MPI::Is_initialized
     */
    static bool initialized()
    { return MPI::Is_initialized(); }

    /*! \brief Wrapps MPI::Finalize
     */
    static void finalize();

    /*! \brief Wrap MPI::Is_finialized
     */
    static bool finalized()
    { return MPI::Is_finalized(); }

    /*! \brief Wrapps MPI::Comm::Get_rank
     *  \param comm: The communicator to use.
     *  \return: The rank of this process within the given communicator.
     */
    static int rank(const MPI::Intracomm & comm=MPI::COMM_WORLD)
    { return comm.Get_rank(); }

    /*! \brief Wrapps MPI::Comm::Get_size
     *  \param comm: The communicator to use.
     *  \return: The sise of the communicator (the total number of processes).
     */
    static int size(const MPI::Intracomm & comm=MPI::COMM_WORLD)
    { return comm.Get_size(); }

    /*! \brief Wrapps MPI::Comm::Barrier, syncronizing processes within
     *         the given communicator.
     *  \param comm: The communicator to use.
     */
    static void barrier(const MPI::Intracomm & comm=MPI::COMM_WORLD)
    { return comm.Barrier(); }

    /*! \brief Returns true if the calling process is the master.
     */
    static bool is_master(const MPI::Intracomm & comm=MPI::COMM_WORLD)
    { return (rank(comm) == 0); }

};


#endif // __MPIWRAPPER__

