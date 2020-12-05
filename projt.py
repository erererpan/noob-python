import androidhelper
droid = androidhelper.Android()
droid.toggleBluetoothState (True)
droid.dialogCreateAlert('Be a server?')
droid.makeToast('ohayou')