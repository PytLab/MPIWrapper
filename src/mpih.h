/*! \file mpih.h
 *  \brief Common MPI header wrapper for serial or parallel builds.
 *
 *  \author ShaoZhengjiang
 *  \contact shaozhengjiang@gmail.com
 */


#ifndef __MPIH__
#define __MPIH__


// NOTE: The RUNMPI flag is set from CMake. It is defined in the
//       CMake generated file mpiflag.h
#include "mpiflag.h"


#if RUNMPI == true
#include <mpi.h>
#else
// Redefine namespace of MPI for serial version builds.
namespace MPI
{
    struct PsudoIntracomm
    {
        int Get_rank() { return 0; }
        int Get_size() { return 1; }
        void Barrier() { return; }
    }

    // Redefine the type of MPI intra-communicator.
    typedef PsudoIntracomm Intracomm;
    static PsudoIntracomm COMM_WORLD;

    // Redefine MPI interfaces.
    void Init() { return }
    void Finalize() { return };
    bool Is_initialized() { return false; }
    bool Is_finalized() { return true; }
}
#endif // RUNMPI

#endif // __MPIH__

