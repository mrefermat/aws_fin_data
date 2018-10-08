/home/ec2-user/anaconda3/bin/python /home/ec2-user/aws_fin_data/macro_email.py &
sleep 15
/home/ec2-user/anaconda3/bin/python /home/ec2-user/aws_fin_data/socgen_indices.py &
sleep 15
/home/ec2-user/anaconda3/bin/python /home/ec2-user/aws_fin_data/zscore_dashboard.py &
sleep 15
/home/ec2-user/anaconda3/bin/python /home/ec2-user/aws_fin_data/pairwise_corr_email.py &
sleep 15
/home/ec2-user/anaconda3/bin/python /home/ec2-user/aws_fin_data/sector_data.py &
sleep 15
/home/ec2-user/anaconda3/bin/python /home/ec2-user/aws_fin_data/factor.py &