import matplotlib.pyplot as plt
import RandomForestsDataCompletion as rfc  # to reference these variables say rfc.variablename

actual1 = rfc.cd['TempMinAbs'].tail(int(len(rfc.cd['TempMinAbs'])*(4260/10648)))
plt.plot(range(1, 4261), rfc.TempMinAbs_Pred, "g-", label='Prediction')
plt.plot(range(1, 4261), actual1, "b-", label='Actual')
plt.title('Temp Min Abs')
plt.ylabel('^0 C')
plt.xlabel('Data Points')
plt.legend()
plt.show()


'''
# create values for x, leaving out the date column and the location column
column_names = ['TempMinAbs', 'TempProm', 'TempMaxAbs', 'Hum', 'Precipitacion', 'RadSolar', 'RadSolarMaxAbs', 'IndiceUV',
                'IndiceUVMaxAbs', 'VientoX', 'VientoY']
# start a for loop  containing the random forests
for x in column_names:
    actual = rfc.cd[x].tail(int(len(rfc.cd[x])*(4260/10648)))
    z = x + '_Pred'
    plt.plot(range(1, 4261), rfc.z, "g-", label='Prediction')
    plt.plot(range(1, 4261), actual, "b-", label='Actual')
    plt.title(x)
    plt.ylabel('units)')
    plt.xlabel('Data Points')
    plt.show()
'''
