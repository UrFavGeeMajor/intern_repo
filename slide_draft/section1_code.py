import graphviz

def create_satellite_diagram():
    """
    Creates and renders a diagram of a satellite communication system
    """
    # Create a new directed graph
    dot = graphviz.Digraph('SatelliteSystem', comment='Satellite Communication Diagram')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define Nodes ---
    # We use '\n' to create line breaks in the labels.
    dot.node('nms', 'Network\nManagement System (NMS)', fillcolor='lightgrey')
    dot.node('feeder', 'Feeder Terminal\n(Gateway)', fillcolor='lightblue')
    dot.node('satellite', 'Satellite\n(Transponder)', shape='ellipse', fillcolor='lightyellow')
    dot.node('ut', 'User Terminal\n(UT)', fillcolor='lightgreen')
    # The 'End Device' has a white fill, so we can set it explicitly or rely on the default.
    dot.node('end_device', 'End Device\n(TV, PC)', fillcolor='white', style='rounded,filled')

    # --- Define Edges with Labels ---
    dot.edge('nms', 'feeder', label=' Mgmt Interface ')
    dot.edge('feeder', 'satellite', label=' Uplink (DVB-S2X) ')
    dot.edge('satellite', 'ut', label=' Downlink (DVB-S2X) ')
    dot.edge('ut', 'end_device', label=' Local Output ')

    # Render the graph to a file and open it automatically
    output_filename = 'satellite_system_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_return_link_diagram():
    """
    Creates and renders a diagram of a satellite return link communication system
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('SatelliteReturnLink', comment='Satellite Return Link Diagram')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes ---
    # The nodes are defined in the order they appear in the flow.
    # We use '\n' to create line breaks in the labels for a clean look.
    dot.node('end_device', 'End Device\n(PC, Phone)', fillcolor='white')
    dot.node('ut', 'User Terminal\n(UT)', fillcolor='lightgreen')
    dot.node('satellite', 'Satellite\n(Transponder)', shape='ellipse', fillcolor='lightyellow')
    dot.node('feeder', 'Feeder Terminal\n(Gateway)\n(FT / GW)', fillcolor='lightblue')
    dot.node('isp', 'Internet /\nService Provider', fillcolor='white')

    # --- Define the Edges (Connections) with Labels ---
    dot.edge('end_device', 'ut', label=' Local Input ')
    dot.edge('ut', 'satellite', label=' Uplink (DVB-RCS2) ')
    dot.edge('satellite', 'feeder', label=' Downlink ')
    dot.edge('feeder', 'isp', label=' Backhaul / IP Core ')

    # Render the graph to a file and open it automatically
    output_filename = 'satellite_return_link_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_dvbs2x_flow_diagram():
    """
    Creates and renders a diagram of the DVB-S2X forward link processing chain,
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('DVBS2X_Flow', comment='DVB-S2X Processing Chain')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes in the Processing Chain ---
    # The nodes are defined with specific colors to match the visual.
    dot.node('gateway', 'Gateway', fillcolor='lightblue')
    dot.node('bbframe', 'BBFRAME', fillcolor='lightyellow')
    dot.node('fec', 'FEC', fillcolor='lightyellow')
    dot.node('modcod', 'MODCOD', fillcolor='lightyellow')
    dot.node('plframe', 'PLFRAME', fillcolor='lightyellow')
    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('terminal', 'Terminal', fillcolor='lightgreen')

    # --- Define the Edges (Connections) to Show the Flow ---
    dot.edge('gateway', 'bbframe')
    dot.edge('bbframe', 'fec')
    dot.edge('fec', 'modcod')
    dot.edge('modcod', 'plframe')
    dot.edge('plframe', 'satellite', label=' Air Interface ')
    dot.edge('satellite', 'terminal')

    # Render the graph to a file and open it automatically
    output_filename = 'dvbs2x_flow_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_dvbrcs2_return_link_diagram():
    """
    Creates and renders a diagram of the DVB-RCS2 return link processing chain,
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('DVBRCS2_Return_Flow', comment='DVB-RCS2 Return Link Processing Chain')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes in the Processing Chain ---
    # The nodes are defined with specific colors to match the visual.
    dot.node('terminal', 'Terminal (RCST)', fillcolor='lightgreen')
    dot.node('mac', 'MAC', fillcolor='lightyellow')
    dot.node('scheduler', 'Scheduler/NCC', fillcolor='lightyellow')
    dot.node('carrier', 'Return Carrier', fillcolor='lightyellow')
    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('gateway', 'Gateway', fillcolor='lightblue')

    # --- Define the Edges (Connections) to Show the Flow ---
    dot.edge('terminal', 'mac')
    dot.edge('mac', 'scheduler')
    dot.edge('scheduler', 'carrier')
    dot.edge('carrier', 'satellite', label=' Uplink ')
    dot.edge('satellite', 'gateway')

    # Render the graph to a file and open it automatically
    output_filename = 'dvbrcs2_return_link_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_forward_link_processing_diagram():
    """
    Creates and renders a diagram of the forward link processing chain,
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('ForwardLinkProcessing', comment='Forward Link Processing Chain')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes in the Processing Chain ---
    # The nodes are defined with specific colors and text to match the visual.
    dot.node('gateway', 'Gateway', fillcolor='lightblue')
    dot.node('bb_processor', 'BB Processor', fillcolor='lightyellow')
    dot.node('fec', 'FEC', fillcolor='lightyellow', shape='octagon')  # Using octagon for a slightly different look
    dot.node('modulator', 'Modulator', fillcolor='lightyellow')
    dot.node('satellite', 'Satellite\n(Transparent Repeater)', shape='ellipse', fillcolor='lightyellow')
    dot.node('demodulator', 'Demodulator', fillcolor='lightyellow')
    dot.node('terminal', 'Terminal\n(Demodulates & decodes PLFRAME)', fillcolor='lightgreen')

    # --- Define the Edges (Connections) to Show the Flow ---
    dot.edge('gateway', 'bb_processor')
    dot.edge('bb_processor', 'fec')
    dot.edge('fec', 'modulator')
    dot.edge('modulator', 'satellite', label=' Uplink ')
    dot.edge('satellite', 'demodulator', label=' Downlink ')
    dot.edge('demodulator', 'terminal')

    # Render the graph to a file and open it automatically
    output_filename = 'forward_link_processing_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_return_link_flow_diagram():
    """
    Creates and renders a diagram of the return link processing chain,
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('ReturnLinkFlow', comment='Return Link Flow Diagram')
    dot.attr(rankdir='LR', splines='line')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the Nodes in the Processing Chain ---
    # The nodes are defined with specific colors and text to match the visual.
    dot.node('rcst', 'RCST\n(Packages data into bursts)', fillcolor='lightgreen')
    dot.node('burst_framing', 'Burst Framing', fillcolor='lightyellow')
    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('hub_demod', 'Hub Demod', fillcolor='lightyellow')
    dot.node('ncc', 'NCC\n(Central Scheduler)', fillcolor='lightblue')

    # --- Define the Edges (Connections) to Show the Flow ---
    dot.edge('rcst', 'burst_framing')
    dot.edge('burst_framing', 'satellite', label=' Uplink (Time-shared using TDMA) ')
    dot.edge('satellite', 'hub_demod', label=' Downlink ')
    dot.edge('hub_demod', 'ncc')

    # Render the graph to a file and open it automatically
    output_filename = 'return_link_flow_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_end_to_end_overview_diagram():
    """
    Creates and renders a diagram of the end-to-end satellite communication system,
    """
    # Create a new directed graph, laying it out from Left to Right.
    dot = graphviz.Digraph('EndToEndOverview', comment='End-to-End System Overview')
    # Using 'compound=True' allows edges to connect to clusters.
    dot.graph_attr.update(rankdir='LR', splines='line', compound='true')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Ground Segment (Hub) ---
    # We use a cluster to group the Gateway and NCC together.
    with dot.subgraph(name='cluster_ground') as c:
        c.attr(label='Ground Segment (Hub)', style='filled', color='lightgrey')
        c.node('gateway', 'Gateway', fillcolor='lightblue')
        c.node('ncc', 'NCC\n(Scheduler)', fillcolor='lightblue')

    # --- Satellite ---
    dot.node('satellite', 'Satellite\n("Bent Pipe" Repeater)', shape='ellipse', fillcolor='lightyellow')

    # --- User Terminal ---
    dot.node('terminal', 'User Terminal (RCST)', fillcolor='lightgreen')

    # --- Define the Edges (Connections) to Show the Flow ---
    # The ltail/lhead attributes connect the edges to the cluster boundaries.
    dot.edge('gateway', 'satellite', label=' Forward Link (DVB-S2X) ')
    dot.edge('ncc', 'satellite', label=' Uplink ')
    dot.edge('satellite', 'terminal', label=' Downlink ')
    # The return link arrow points from the terminal back to the satellite.
    dot.edge('terminal', 'satellite', label=' Return Link (DVB-RCS2) ', dir='back')

    # Render the graph to a file and open it automatically
    output_filename = 'end_to_end_overview_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")

# Run the function to create the diagram
if __name__ == "__main__":
    pass
