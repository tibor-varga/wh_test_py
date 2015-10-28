#!/bin/bash
# Module:   cmd_line.sh
# Purpose:  cmd line python tests
# Date:     N/A
# Notes:    
# 1)  Shell->Python test code
# 2)  Uses Python's stat to get the size of a file....
# 3)  Ref:
#       http://stackoverflow.com/questions/2802726/putting-a-simple-if-then-statement-on-one-line
PY=`ls -1 *.py`
for fn in $PY; do
    echo "FN=" $fn
    python -c "import os, sys; F=\"$fn\"; size=os.stat(F).st_size; print \"File=\", F, \"Size=\", size"
done

echo "-----------------------------------------------------------------------------"
echo " IF test using Python's ternary operator "
F=cmd_line.sh
python -c "print 'F=', \"$F\"; x='found' if \"$F\"=='cmd_line.sh' else 'not found'; print 'x=', x"

echo "-----------------------------------------------------------------------------"
echo "Math test"
Q=3
python -c "import math; print \"Q=\", $Q; qq=math.cos(math.pi*$Q); print \"res=\", qq"

