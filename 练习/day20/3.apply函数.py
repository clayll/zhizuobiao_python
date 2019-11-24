import numpy as np
import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1':[43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2':[24, 63, 56, 56, 67, 51, 79, 46, 72, 60],
          },

    index= ['Andre','Barry','Chris','Dan','Emily','Fred','Greta','Hubert','Ivan','James']
)


def convert_grades_curve(exam_grades):
    return pd.qcut(exam_grades,[0, 0.1,0.2,0.5,0.8,1],labels=['E','D','C','B','A'])

print(grades_df.apply(convert_grades_curve))
#apply()里的axis属性  axis=0列，axis=1行

