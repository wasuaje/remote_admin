PySSH 0.3 Notes

PySSH has been restructured as a python "package". That means it will
install all its files in its own directory under 'site-packages'

A Distutils setup.py is included for building binary packages. Using
binary packages is encouraged as it promotes better software 
configuration management. (For more information on Distutils, see
http://www.python.org/sigs/distutils-sig )

As Distutils does not support Debian packages, Debian packaging files are
also included in the debian subdirectory. See debian/READM for inforation
on creating binary Debian packages

New Features
Version 0.3 adds fssa.py. fssa.py works to a Find Secure Shell Agent
to use rather than prompt the user for authentication information. 
This makes PySSH more useful for batch/cron jobs. For more information
on using ssh, and consequently PySSH in batch and cron jobs, see 
http://www.ucolick.org/~sla/ssh/sshcron.html

PySSH 0.2 Notes

PySSH includes three components.
pyssh.py: the main library to be imported
nbpipe.py: a library to emulate a non-blocking pipe under Windows
               (and used in posix environments to be consistent)
ptyext.py: a modified and extended version of the stardard pty.py library

These are all licensed under a Python 2.2 style license.  See license.txt.
This basically means you can use them and distribute them pretty freely,
even in a closed source manner.

--------------------------------------

HISTORY

PySSH was a project started by Chuck Esterbrook in August 2001.
He wrote version 0.1, and set up the project on Sourceforge.

After some initial development, Chuck found that he had other
projects that he wanted to be working on.

In August 2002, I found the project, and offered to take on
maintanence of the project.  Due to some unresolved issues in
the original code, I found it necessary to re-write the project
from the bottom up.  I drew on ideas from Chuck's original code,
as well as ideas from code by Julian Schaefer-Jasinski and Guido's
telnetlib, and created version 0.2.

--------------------------------------

NOTES and KNOWN ISSUES 

Under Linux it should probably be considered beta quality.
As far as I can tell it works.  Let me know otherwise.

Under Windows it is alpha quality.

Known issues under Windows:
There is no way of killing the connection. plink does not seem to have any
escape code to terminate the connection, and there is no 'kill' command
in python for windows.  My plan is to implement a version of popen2 under
Windows using the win32all python library, which will return the windows
PID and allow killing of the process.  If someone else wishes to do this,
it may happen sonner rather than later.

That being said, on well behaved connections that exit normally (such as
by sending an 'exit' or 'logout' command), PySSH should work fine on Windows
too.

Under Cygwin - well, I'm unsure whether it is alpha or beta.  You test it
and let me know.  :-)

Known issues under Cygwin:
Unlike in Linux where importing signal causes the keyboard interrupt
to be handled by the main thread, under Cygwin it seems to be caught randomly.
There may be little that can be done about this problem.  It is mainly an issue
in the test() routine anyway.
However, the close() function does work under Cygwin, and so should be okay for
general use from other code.

Future plans:
(0) Re-implement setup.py as per version 0.1, and create new documentation.
(1) Implement a way of forcing a close under Windows (using win32all).
(2) If (1) is done, then possibly drop the non-blocking pipe using a thread
arrangement, and move to using select on posix systems, and the equivalent
win32all function under windows.
(3) Improve the API?
(4) Who knows....

PySSH is currently hosted at SourceForge.
http://sourceforge.net/projects/pyssh

You should be able to find the latest version there, and a mailing list
to discuss any problems, ideas, solution etc.

Rasjid Wilcox
6 September 2002

