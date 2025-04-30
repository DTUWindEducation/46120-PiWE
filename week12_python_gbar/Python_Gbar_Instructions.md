# Welcome to a parallel run of `turbie`

A complete understanding of how parallelism works is
far from what we can achieve today, however, we would
like you to be able to critically think how to apply
parallism to your workflows, and be able to analyze
whether or not it makes sense to parallelize a given
task.
 
We don't have too much time, so basically everything is
prepared for you.
It is a little(read highly) dense, since there are many small points
that is necessary for you to learn.

You will be asked to do the following:

1. Login to our High-Performance Computing
   facilities. 

  * Access to the DTU Gbar HPC system
  * Secure Shell (ssh) connection
  * Access with your DTU username & password only from a DTU network

2. We will look into how to create *virtual environments*.
   
   Todays exercises will be based on locally installed
   environments. Frequently, users will have to adapt
   to new systems, and navigating several installations
   is easily managed using virtual environments.

   (you are already familiar with conda, which does the
   same thing, but slightly differently)

3. Once you have a running example of `turbie` we will dig
   a bit into how to create a submit script so one can
   *dispatch* your jobs.

After the exercises today, you will know how to
- create virtual environments containing specific packages
- understand how to submit a batch job on the HPC facility
- understand that throwing more CPU's won't necessarily
  mean better performance. Understanding your application
  and testing is VITAL!


## Logging into the HPC facility

Please login to the HPC facility by using the ssh.

- `ssh <dtu student id>@login.hpc.dtu.dk`

- connect; your shell should show something like this: 
  
      gbarlogin1$ 
  
  This means you are currently running on our login server.
  This is a server meant for people to access the cluster,
  you should avoid running tasks taking more than a few minutes
  here.


## Installing Python packages in a virtual environment

Virtual environments for Python is a handy way to have
multiple packages of various versions installed simultaneously.

There exists a great variety of tools to manipulate them, here
we use the default (available in all Python installations) [`venv` library](https://docs.python.org/3/library/venv.html).

0. Step zero is to jump into an interactive node ASAP by typing `linuxsh`

1. On our HPC system the default Python 3 version is 3.6.8.
   This is too old!

   Our HPC infrastructure uses *modules* to easily swap between
   different software versions.
   (NOTE: This needs to be done everytime one wishes to use a
   specific software version, hence closing the shell would
   force one to load the same modules *again*).

   Do
   
       module load python3/3.11.7

  Any problem with the specific version? To check all the available version you can run:

      ml av
   
   now having the right version of Python, you can check:
   
       $> python3 --version
       Python "version"
   
   should be shown.

2. Once you have loaded the desired Python version, we can create
   the virtual enviroment:
   
       python3 -m venv turbie # argument can be any name you wish
   
   This will create a new folder called `turbie` which
   will always use the same Python version as was used
   to create it with, in this case 3.11.8.

3. Every time one wishes to use an enviroment, one should
   *activate* it.
   
       source turbie/bin/activate
   
   now your shell should look a little different, you
   should see `(turbie)` prefixed on your command line.

   Now, every `python3` and `pip3` command will be
   issued using this virtual enviroment.
   Hence, installing any packages will only happen
   in this sub-folder (it won't affect any other environments).

4. For the exercises here, we should install some packages.
   First ensure that you have activated the environment.

   Now do:
   
       pip3 install numpy scipy
   
   and you should be ready to go!
   (You can always later install more packages)


Since a virtual environment is a folder, it is easy to
see that you can have as many virtual environments as
you want.

(In `conda`, environments also exists, they are
basically the same thing, albeit with some smaller
differences)

It is also easy to delete an environment, simply
delete the folder.


## Using the batch system

The HPC infrastructure uses a batch system to distribute
resources.
The infrastructure, however, needs to know some details
about the program and execution, e.g.:
- ETA for the completion of the job (needs to be a bit more
  than anticipated so one is sure the job will complete)
- how much memory the job will use
- how many CPU cores the job will have access to
- ... there may be many other configurations

A jobscript is nothing but a shell script which contains
some annotated fields that the scheduler parses, and
the rest is a regular script.
(NOTE: read more details on how to do bash-scripting,
it can greatly relieve common workflows.)
The annotated fields *must* exist as comments (without
spaces in between), and each annotated field should
start with a single `#` character.

For instance if your code wants to run for 10 hours, use
2GB per core and use 6 cores, an example job script would
contain these fields:

    # This is a regular comment
    #BSUB -W 10:00
    #BSUB -n 6
    # Note, the total reserved memory will be 6*2GB = 12GB
    #BSUB -R "rusage[mem=2GB]"

More details for the submit script can be found [here](https://www.hpc.dtu.dk/?page_id=1416).

To submit a job, one needs to pipe in the script to the
`bsub` command, and then it will be dispatched for
execution (when resources get free):

    # please note the "<" which *pipes* the content of 
    # script.sh into the `bsub` command
    bsub < script.sh

There are many details on using a scheduler, here
we simply show you the most basic things, but encourage
you to read more if interested.


When submitting a job, you typically have to wait
until the HPC has *free* resources that may be used
to execute your job. When requesting a lot of resources
you may wait longer than when requesting fewer.
The idea is that you can submit hundres of jobs (or more)
and then each of them will be runned when resources are free.
If resources are plentyful, then possibly concurrently!

For more information on how to view running/scheduled
jobs, please see [here](https://www.hpc.dtu.dk/?page_id=1519).


## Running turbie examples

The exercises for today will consist of codes
pre-done for you.

- unpack the exercises from today using:

      tar xfz /work3/nicpa/teaching/SPP/2024/SPP_week11.tar.gz

  this will unpack the content of the file in the current folder.
  You should see a folder named `SPP_week11`.

- `run_turbie.py` is a set of scripts
  that makes the exercise codes easier to understand.
  It is not critical that you understand this file.

  It contains wrappers for the `turbie.py`
  code and will enable quick reading of data-files
  and quick solving of data-sets as mandated by the
  `turbie` code.

  You can run this just like a normal script, or
  you can import the functions defined in it.
  The following script you will use
  will import the functions defined in this
  code.

- `run_turbie_parallel.py` is a code to run `turbie`
  in parallel.
  
  `turbie` is using `numpy` and `scipy` under the
  hood. This means that the code *may* use threaded
  libraries, such as BLAS and/or LAPACK.
  A threaded library can spawn threads that allows
  a certain level of parallelism.
  Generally, threaded high-performance libraries
  will use OpenMP threads. The number of OpenMP
  threads can be controlled via this environment
  variable:

      OMP_NUM_THREADS=<integer>

  E.g. if one wants to run `turbie` and allow `numpy/scipy`
  to use 4 threads, one would do:

      OMP_NUM_THREADS=4 python3 run_turbie_parallel.py

  Alternatively one can do:

      export OMP_NUM_THREADS=4
      python3 run_turbie_parallel.py # will use 4 threads

  which would store the `OMP_NUM_THREADS` variable
  until the shell is over (if you close the terminal
  and re-open it, the `OMP_NUM_THREADS` variable will be
  reset to its default).

  By default `OMP_NUM_THREADS` will be unset, meaning that
  it is the application that allows one to default to all
  or 1 core.
  On our HPC facility, the default value of `OMP_NUM_THREADS`
  is 1.


  Secondly, the parallel code can be runned in parallel mode.

      python3 run_turbie_parallel.py n <integer>
  
  The `n <integer>` clause enables one to select how many cores
  one wishes to parallelize over.
  Note, that this is in addition to the number of threads
  the `numpy/scipy` code will utilize.
  
  For instance:
  
      OMP_NUM_THREADS=3 python3 run_turbie_parallel.py n 2
  
  will launch 2 processors, each of these will use 3 threads.
  This will result in 6 simultaneous processes. If all are fully
  utilized, you would need 6 cores for the best efficiency.
  (Consider the case where your computer only has 2 cores, that would
  mean that the 6 processes would battle for resources! Not ideal!)

  Here is a simple analog for how the different parallelisms work:

      # processors can be used to parallelize the loop
      for i in range(10):
          # threads(OMP_NUM_THREADS) are used to distribute
          # the matrix operations
          C[i] = A[i] @ B[i]

  hence processors is useful if the outer loop is *large* (or
  if the amount of work being done *in* the loop is *large*),
  and threads are useful when the amount of work for the matrix
  operations is *large*.

  There is no single definition of *large*. It all depends,
  generally you should do some benchmarks of your code
  to see how well it scales.
  On the other hand, throwing too many resources at a very small
  problem has the downside of taking more time than running it
  in serial.

  Why is this? (is splitting tasks cost-free?)

  Parallelism is not easy, there are many more pitfalls than what
  we show here.

  We also know that the terminology, processors, processes and threads
  may be confusing. [Search around for more details](https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread).


# Exercises

The exercises for today are:

1. Extracting the exercises for today

   Follow the instructions in the previous section. 

2. Submitting a batch job. This will teach you to
   submit and see how a job may be dispatched.

   Also run the scripts locally, which is faster?
   Can you directly compare your own computer timings
   with a HPC server?
   Can you compare with your peers timings?

   Why? Why not?

   Note the use of the `OMP_NUM_THREADS` variable
   when running locally.

3. Copy the timings files from the exercise folder today
   (`ref_timings` folder)
   to your own computer. This will allow you to analyse
   some test results, while waiting for your own results.
   
   Read the code `parse_output.py` and understand how
   it parses the timing files from the submit script.
   Notably, it should be runned while in the directory
   of the output files.

        cd ref_timings
        python3 ../parse_output.py

   The end of the file contains some examples on how
   to plot the data. Try to:

   1. Add the plotting of the line that corresponds to
      `OMP_NUM_THREADS=2`.

   2. Change the script so it can *also* plot speed-up curves.
      A speed-up curve is basically `time_1 / time_P`.

      - `time_1` is the time it took to execute the
        code using 1 processor.
      - `time_P` is the time it took to execute the
        code using P processors.

      In a naive world, how would you expect this curve
      to look?

   3. Try and plot for various fixed `OMP_NUM_THREADS`
      and see how the speed-up looks.

   Carefully discuss with your peers why you see
   what you see.
   Consider how many files you process
   (HINT: outer loop),
   how much data is in each of these files (HINT: inner loop).

   Can you guess what would happen for the plot if you had
   fewer/more files to process? 

   Can you guess what would happen for the plot if you had
   more data in each file to process? 


## Extra exercises

1. Run a new job by removing some of the files (so you only have
   8-10 files). That would
   reduce the *outer loop*.
   Submit the batch job and re-analyse the data.
   
   What happens?

2. Run a new job by adding more files (so you have around 100 files).
   This will increase the *outer loop*.
   Submit the batch job and re-analyse the data.
   
