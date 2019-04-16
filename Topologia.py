from mininet.topo import Topo
class MyTopo( Topo ):
    "Simple topology example." 
  def __init__( self ):
        "Create custom topo."
        # Initialize topology
        Topo.__init__( self )
        # Add hosts and switches
        Host1 = net.addHost( 'h1', ip='10.0.0.1', mac='00:00:00:00:00:01' )
        Host2 = net.addHost( 'h2', ip='10.0.0.2', mac='00:00:00:00:00:02' )
        Host3 = net.addHost( 'h3', ip='10.0.0.3', mac='00:00:00:00:00:03' )
        Host4 = net.addHost( 'h4', ip='10.0.0.4', mac='00:00:00:00:00:04')
	ServerWeb = net.addHost( 'SrvWeb', ip='10.0.0.5', mac='00:00:00:00:00:05' )	
        Switch1 = self.addSwitch( 's1' )
        Switch2 = self.addSwitch( 's2' )
        # Add links
        self.addLink( Host1, Switch1 )
        self.addLink( Host2, Switch1 )	
	self.addLink( Host3, Switch1 )
        self.addLink( Switch1, Switch2 )
       self.addLink( Switch2, Host4 )
        self.addLink( Switch2, ServerWeb )
topos = { 'mytopo': ( lambda: MyTopo() ) }
