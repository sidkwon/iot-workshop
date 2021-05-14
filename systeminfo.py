#!/usr/bin/env python3
import psutil

def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    :returns: System CPU load as a percentage.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5)
    
def get_ram_usage_pct():
    """
    Obtains the system's current RAM usage.
    :returns: System RAM usage as a percentage.
    :rtype: float
    """
    return psutil.virtual_memory().percent
    
def get_swap_usage_pct():
    """
    Obtains the system's current Swap usage.
    :returns: System Swap usage as a percentage.
    :rtype: float
    """
    return psutil.swap_memory().percent

def main():
    # Output current CPU load as a percentage.
    print('System CPU load is {} %'.format(get_cpu_usage_pct()))
    # Output current RAM usage as a percentage.
    print('RAM usage is {} %'.format(get_ram_usage_pct()))
    # Output current Swap usage as a percentage.
    print('Swap usage is {} %'.format(get_swap_usage_pct()))

    
if __name__ == "__main__":
    main()