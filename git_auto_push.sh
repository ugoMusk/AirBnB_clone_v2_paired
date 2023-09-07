#!/bin/bash
echo git_auto_push.sh >> ../.gitignore
list=`ls $(pwd)`

for i in $list;
do n=$(grep -oE "^|\.[a-z]{1,5}$" <<< $i) && bn=$(basename -s "$n" $i) && git add $i && git commit -m "update $bn" && git push;
done
