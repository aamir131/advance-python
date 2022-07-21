from logging import*
Log_Format = '{lineno} *** {name} *** {asctime} *** {message}'
basicConfig(filename='logfile.log',level=DEBUG,filemode='w',style = '{',format=Log_Format)
log = getLogger('Mak')

log.warning('This is warning')
log.info('This is info')
log.debug('This is debug')
log.critical('this is critical')
log.error('This is error')