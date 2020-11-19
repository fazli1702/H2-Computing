SELECT Device.SerialNumber, Device.Model, Device.location, Monitor.DateCleaned
FROM Device, Monitor WHERE Device.SerialNumber = Monitor.SerialNumber
