#!/usr/bin/env python

# Simple test of common functionallity. We don't jet test correctness of
# results (i.e. compare numbers).

import subprocess as sp
import os
import shutil



def system(call):
    print("[system] calling: %s" %call)
    proc = sp.Popen(call, shell=True)    
    os.waitpid(proc.pid, 0)

if __name__ == '__main__':
    
    print("*"*78)
    print("testing cmd line")
    print("*"*78)

    infile = "AlN.md.in"
    outfile = "AlN.md.out"
    outfile_gz = outfile + '.gz'
    outdir = "/tmp/test_pdos"
    exe = '../lib/pydos.py'

    calls =[]
    calls.append("%s -i %s -o %s -x %s -p" %(exe, infile, outfile_gz, outdir) )
    calls.append("%s -i %s -o %s -x %s -d -m -M" %(exe, infile, outfile_gz, outdir))

    for call in calls:
        system(call)

    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    
    #------------------------------------------------------------------------

    print("*"*78)
    print("testing import of pwtools package")
    print("*"*78)
    
    # Modify PYTHONPATH so that we import from the current branch.
    os.environ['PYTHONPATH'] = os.path.abspath('../../')
    print "modified os.environ['PYTHONPATH']:", os.environ['PYTHONPATH']
    system('cd $HOME && python -c "import pwtools"')