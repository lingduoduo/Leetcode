

export PGHOST=prod-redshift-analytics-a-cluster-nn1yea2mx2aq.caynbckl0itc.us-west-2.redshift.amazonaws.com

export PGUSER=ling.huang
 
export PGPASSWORD=A59466d0-92f5-4208-9997-9086f0dc3e9e
 
export PGPORT=5439
 
export PGDATABASE=dev
 

create user "ling.huang"  with password 'A59466d0-92f5-4208-9997-9086f0dc3e9e'
in group developersgroup_readonly;


