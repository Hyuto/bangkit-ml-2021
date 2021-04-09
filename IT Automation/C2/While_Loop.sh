START=1
STOP=10
while [ $START -le $STOP ]; do
    echo "Counting on $START from $STOP"
    ((START+=1))
done