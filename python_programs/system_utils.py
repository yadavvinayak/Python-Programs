#create a function that can be reuse, it should show system info

import psutil

def get_system_details():
    cpu= psutil.cpu_percent(interval=1)
    memory= psutil.virtual_memory().percent
    disk= psutil.disk_usage("/").percent

    system_info= {
        "CPU": cpu,
        "Memory": memory,
        "Disk": disk
    }
    
    return(system_info)



