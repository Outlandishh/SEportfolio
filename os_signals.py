# Import all relevant libraries that are needed
import signal
import os
import time
import sys


# Function used to read the SIGHUP signal
def readConfiguration(signalNumber, frame):
    print('(SIGHUP) reading configuration')
    return


# Function to end the process
def terminateProcess(signalNumber, frame):
    print('(SIGTERM) terminating the process')
    sys.exit()


# Function to receive a signal from terminal
def receiveSignal(signalNumber, frame):
    print('Received:', signalNumber)
    return


# Register the signals that are to be caught
if __name__ == '__main__':
    signal.signal(signal.SIGHUP, readConfiguration)
    signal.signal(signal.SIGINT, receiveSignal)
    signal.signal(signal.SIGQUIT, receiveSignal)
    signal.signal(signal.SIGILL, receiveSignal)
    signal.signal(signal.SIGTRAP, receiveSignal)
    signal.signal(signal.SIGABRT, receiveSignal)
    signal.signal(signal.SIGBUS, receiveSignal)
    signal.signal(signal.SIGFPE, receiveSignal)
    # signal.signal(signal.SIGKILL, receiveSignal)
    signal.signal(signal.SIGUSR1, receiveSignal)
    signal.signal(signal.SIGSEGV, receiveSignal)
    signal.signal(signal.SIGUSR2, receiveSignal)
    signal.signal(signal.SIGPIPE, receiveSignal)
    signal.signal(signal.SIGALRM, receiveSignal)
    signal.signal(signal.SIGTERM, terminateProcess)

    # Output current process ID
    print('My PID is:', os.getpid())

    # Wait in an endless loop for signals
    while True:
        print('waiting...')
        time.sleep(5)