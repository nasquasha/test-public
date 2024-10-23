if (work>low_work_limit)&(work<high_work_limit)&(override=='bad')&(best_corr>best_corr_limit)&(ydiff<high_ydiff_limit):
 return 'good'
else:
 return override
