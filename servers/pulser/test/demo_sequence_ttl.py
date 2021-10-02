import labrad
from labrad.units import WithUnit
with labrad.connect() as cxn:
    duration = WithUnit(100, 'ms')
    pulser = cxn.pulser
    pulser.new_sequence()
    channels = pulser.get_channels()
    channel_names = [chan[0] for chan in channels]
        
    #print channel_names
    
#     for i in range(len(channels)):
#         start = i * duration
#         pulser.add_ttl_pulse((channel_names[i],  start , duration))

    pulser.add_ttl_pulse('ttl_0',WithUnit(0,'ms'),WithUnit(1,'ms'))
    #pulser.add_ttl_pulse('ttl_0',WithUnit(2000,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('ttl_0',WithUnit(1000,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('ttl_0',WithUnit(1500,'ms'),WithUnit(250,'ms'))
    
    #pulser.add_ttl_pulse('sMOT_PROBE',WithUnit(0,'ms'),WithUnit(250,'ms'))
    pulser.add_ttl_pulse('sMOT_PROBE',WithUnit(1,'ms'),WithUnit(1,'ms'))
    #pulser.add_ttl_pulse('sMOT_PROBE',WithUnit(1750,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('sMOT_PROBE',WithUnit(750,'ms'),WithUnit(250,'ms'))
    
    #pulser.add_ttl_pulse('sMOT_PROBE_SPIN',WithUnit(500,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('sMOT_PROBE_SPIN',WithUnit(1500,'ms'),WithUnit(250,'ms'))

    pulser.add_ttl_pulse('BIG_MOT_SH',WithUnit(0,'ms'),WithUnit(200,'ms'))
    #pulser.add_ttl_pulse('BIG_MOT_SH',WithUnit(500,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('BIG_MOT_SH',WithUnit(1250,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('BIG_MOT_SH',WithUnit(750,'ms'),WithUnit(250,'ms'))
    
    #pulser.add_ttl_pulse('sMOT_AO',WithUnit(1000,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('BIG_MOT_AO',WithUnit(1250,'ms'),WithUnit(250,'ms'))
    #pulser.add_ttl_pulse('405_ECDL',WithUnit(1500,'ms'),WithUnit(250,'ms'))
    
    #pulser.add_ttl_pulse('ttl_1',WithUnit(0,'ms'),WithUnit(100,'ms'))
    #pulser.add_ttl_pulse('channel_2',WithUnit(200,'ms'),WithUnit(100,'ms'))
    #pulser.add_ttl_pulse('channel_3',WithUnit(400,'ms'),WithUnit(100,'ms'))
    
    #pulser.add_ttl_pulse('ResetDDS',WithUnit(500,'ms'),WithUnit(1,'ms'))
    
    
#     pulser.program_sequence()
#     
#     ttl = cxn.pulser.human_readable_ttl()
#     sp = SequencePlotter(ttl.asarray,None, channels)
#     sp.makePlot()
        
    pulser.program_sequence()
    pulser.start_number(200)
    pulser.wait_sequence_done()
    pulser.stop_sequence()