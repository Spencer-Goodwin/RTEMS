# RTEMS
# CTF Integration
There are two possible methods for achieving this task.
1. Including external YAML files
2. Creating a barectf platform

Due to the Automake and Makefile implimentation, both methods will have to be implemented. I have produced an example of how the YAML files should be chained and refrenced.

The file named info.yaml will be in the ~/development/rtems/4.12/share directory. RTEMS can be conviently configured to obtain a share folder that can be used to refrence information within an RTEMS build.

Things that need to be done:
1. Populate the info.yaml file with it's own functions.(I used the functions in the buffer just to retrieve *ctx and it does work)
  -This will need to start with the first automake and makefile configuration.
  -The file should not be created until the waf configuration.

2. There needs to be a CTF platform created:
  -This will need to be accomplished because most RTEMS builds already trace, create a buffer, and RTEMS already has an implementation where C functions are produced
  -The C library is in the {prefix}/share/rtems/trace-linker/libc.ini.
