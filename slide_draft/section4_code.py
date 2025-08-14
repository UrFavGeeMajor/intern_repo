import graphviz

def create_final_recap_diagram():
    """
    Creates and renders a final recap diagram showing the complete,
    bidirectional data flow in a DVB-S2X / DVB-RCS2 system.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('FinalRecap', comment='Final Recap Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the main components ---
    dot.node('internet', 'Internet / Core Network', fillcolor='whitesmoke')

    # Ground Segment Cluster
    with dot.subgraph(name='cluster_ground') as c:
        c.attr(label='Ground Segment', style='filled', color='lightgrey')
        c.node('gateway', 'Gateway / NCC', fillcolor='lightblue')

    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('rcst', 'User Terminal (RCST)', fillcolor='lightgreen')

    # --- Define the Edges to show the complete flow ---

    # Internet to Gateway
    dot.edge('internet', 'gateway')

    # Forward Link Path (Gateway -> Satellite -> RCST)
    dot.edge('gateway', 'satellite',
             label=' DVB-S2X Forward Link\n(IP → GSE → BBFRAME → PLFRAME) ')
    dot.edge('satellite', 'rcst', label=' Downlink ')

    # Return Link Path (RCST -> Satellite -> Gateway)
    dot.edge('rcst', 'satellite',
             label=' DVB-RCS2 Return Link\n(Burst → MF-TDMA Slot) ',
             dir='back')
    dot.edge('satellite', 'gateway',
             label=' Downlink to Hub ',
             dir='back')

    # Render the graph to a file and open it automatically
    output_filename = 'final_recap_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_logical_physical_mapping_diagram():
    """
    Creates and renders a diagram illustrating the mapping between
    Logical and Physical channels.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('ChannelMapping', comment='Logical to Physical Channel Mapping')
    dot.attr(rankdir='LR', splines='line', nodesep='1.0', ranksep='2.5')
    dot.attr('node', shape='record', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Left Column: Logical Channels ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='Logical Channels (What is being sent?)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')
        c.attr('node', fillcolor='lightblue')
        # Using record shapes to include icons and text
        c.node('gse_stream', '{🏷️ | GSE Stream (User Data)}')
        c.node('control_ch', '{🏷️ | Control Channel}')
        c.node('signaling_ch', '{🏷️ | Signaling Channel}')

    # --- Right Column: Physical Channels ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='Physical Channels (Where is it being sent?)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        # Using record shapes to include icons and text
        c.node('slot3', '{Slot #3 | 📡}')
        c.node('freq1275', '{Frequency 12.75 GHz | 📡}')
        c.node('modcod16', '{MODCOD 16APSK | 📡}')

    # --- Mapping Edges ---
    dot.edge('gse_stream', 'slot3', label=' Mapped To ')
    dot.edge('control_ch', 'freq1275', label=' Mapped To ')
    dot.edge('signaling_ch', 'modcod16', label=' Mapped To ')

    # Render the graph to a file and open it automatically
    output_filename = 'logical_to_physical_mapping_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_physical_channels_overview_diagram():
    """
    Creates and renders a diagram that provides an overview of Physical Channels
    for DVB-S2X and DVB-RCS2.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('PhysicalChannelsOverview', comment='Physical Channels Overview Diagram')
    dot.attr('node', shape='record', style='rounded,filled', fontname='Helvetica')

    # --- Top Part: Physical Resource Grid ---
    with dot.subgraph(name='cluster_grid') as c:
        c.attr(label='Physical Resource Grid', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')

        # Use an HTML-like table for the grid visual
        grid_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
  <TR><TD BORDER="0" COLSPAN="3" ALIGN="CENTER"><B>Time →</B></TD></TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 1</B></TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">Slot 1</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">Slot 2</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 2</B></TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">Slot 3</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">Slot 4</TD>
  </TR>
</TABLE>>'''
        c.node('grid', grid_label, shape='plain')

    # --- Bottom Part: Physical Channel Examples ---
    with dot.subgraph(name='cluster_channels') as c:
        c.attr(label='Physical Channels (Actual Transmission Resources)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')

        # DVB-RCS2 Examples
        with c.subgraph(name='cluster_rcs2') as rcs2:
            rcs2.attr(label='DVB-RCS2 Examples', style='rounded', color='white')
            rcs2.attr('node', fillcolor='lightgreen')
            rcs2.node('burst', '{Burst Structure | Preamble, Payload, Guard}')
            rcs2.node('mftdma', '{MF-TDMA Slots | Time-Frequency Grid}')

        # DVB-S2X Examples
        with c.subgraph(name='cluster_s2x') as s2x:
            s2x.attr(label='DVB-S2X Examples', style='rounded', color='white')
            s2x.attr('node', fillcolor='lightblue')
            s2x.node('modcod', '{MODCOD | Modulation & Coding}')
            s2x.node('carrier', '{Carrier Frequency | RF Channel}')
            s2x.node('plframe', '{PLFRAME / BBFRAME | Encapsulated Data}')

    # Render the graph to a file and open it automatically
    output_filename = 'physical_channels_visual_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_physical_channels_overview_diagram():
    """
    Creates and renders a diagram that provides an overview of Physical Channels
    for DVB-S2X and DVB-RCS2.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('PhysicalChannelsOverview', comment='Physical Channels Overview Diagram')
    dot.attr(rankdir='TB', nodesep='1.0', ranksep='1.0')  # Top-to-Bottom layout
    dot.attr('node', shape='record', style='rounded,filled', fontname='Helvetica')

    # --- Top Part: Physical Resource Grid ---
    with dot.subgraph(name='cluster_grid') as c:
        c.attr(label='Physical Resource Grid', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')

        # Use an HTML-like table for the grid visual
        grid_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0" CELLPADDING="0">
  <TR><TD BORDER="0" COLSPAN="3" ALIGN="CENTER"><B>Time →</B></TD></TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 1</B></TD>
    <TD BORDER="1" BGCOLOR="#FFCCCC">Slot 1</TD>
    <TD BORDER="1" BGCOLOR="#CCE5FF">Slot 2</TD>
  </TR>
  <TR>
    <TD BORDER="0" ALIGN="RIGHT"><B>Freq 2</B></TD>
    <TD BORDER="1" BGCOLOR="#D4EDDA">Slot 3</TD>
    <TD BORDER="1" BGCOLOR="#FFF3CD">Slot 4</TD>
  </TR>
</TABLE>>'''
        c.node('grid', grid_label, shape='plain')

    # --- Bottom Part: Physical Channel Examples ---
    with dot.subgraph(name='cluster_channels') as c:
        c.attr(label='Physical Channels (Actual Transmission Resources)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')

        # DVB-RCS2 Examples
        with c.subgraph(name='cluster_rcs2') as rcs2:
            rcs2.attr(label='DVB-RCS2 Examples', style='rounded', color='white')
            rcs2.attr('node', fillcolor='lightgreen')
            rcs2.node('burst', '{Burst Structure | Preamble, Payload, Guard}')
            rcs2.node('mftdma', '{MF-TDMA Slots | Time-Frequency Grid}')

        # DVB-S2X Examples
        with c.subgraph(name='cluster_s2x') as s2x:
            s2x.attr(label='DVB-S2X Examples', style='rounded', color='white')
            s2x.attr('node', fillcolor='lightblue')
            s2x.node('modcod', '{MODCOD | Modulation & Coding}')
            s2x.node('carrier', '{Carrier Frequency | RF Channel}')
            s2x.node('plframe', '{PLFRAME / BBFRAME | Encapsulated Data}')

    # Render the graph to a file and open it automatically
    output_filename = 'physical_channels_visual_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_final_recap_diagram():
    """
    Creates and renders a final recap diagram showing the complete,
    bidirectional data flow in a DVB-S2X / DVB-RCS2 system.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('FinalRecap', comment='Final Recap Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Define the main components ---
    dot.node('internet', 'Internet / Core Network', fillcolor='whitesmoke')

    # Ground Segment Cluster
    with dot.subgraph(name='cluster_ground') as c:
        c.attr(label='Ground Segment', style='filled', color='lightgrey')
        c.node('gateway', 'Gateway / NCC', fillcolor='lightblue')

    dot.node('satellite', 'Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('rcst', 'User Terminal (RCST)', fillcolor='lightgreen')

    # --- Define the Edges to show the complete flow ---

    # Internet to Gateway
    dot.edge('internet', 'gateway')

    # Forward Link Path (Gateway -> Satellite -> RCST)
    dot.edge('gateway', 'satellite',
             label=' DVB-S2X Forward Link\n(IP → GSE → BBFRAME → PLFRAME) ')
    dot.edge('satellite', 'rcst', label=' Downlink ')

    # Return Link Path (RCST -> Satellite -> Gateway)
    dot.edge('rcst', 'satellite',
             label=' DVB-RCS2 Return Link\n(Burst → MF-TDMA Slot) ',
             dir='back')
    dot.edge('satellite', 'gateway',
             label=' Downlink to Hub ',
             dir='back')

    # Render the graph to a file and open it automatically
    output_filename = 'final_recap_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_abstraction_reality_diagram():
    """
    Creates and renders a diagram that visually explains the difference
    and mapping between the logical channel view and the physical channel reality.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('AbstractionVsReality', comment='Channel Abstraction vs. Reality Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='0.8', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Top Layer: Logical View (Abstraction) ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='1. Logical View (What the protocol defines)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightblue')
        # Use a record shape to group the logical flows
        c.node('logical_flows',
               '<f0> User Data |<f1> Control |<f2> Signaling',
               shape='Mrecord')

    # --- Bottom Layer: Physical Reality (What happens on air) ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='2. Physical Reality (Actual transmission resources)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        # Use a record shape to group the physical resources
        c.node('physical_resources',
               '<f0> Frame / Slot |<f1> Frequency |<f2> MODCOD',
               shape='Mrecord')

    # --- Callout Box for Dynamic Mapping ---
    dot.node('callout',
             'Same logical flow →\ndifferent physical resource allocation\ndepending on network state.',
             shape='note', fillcolor='lightyellow', style='filled,dashed')

    # --- Mapping Arrows ---
    # From Logical Flows to Physical Resources
    dot.edge('logical_flows:f0', 'physical_resources:f0', label='Mapped to')
    dot.edge('logical_flows:f1', 'physical_resources:f1', label='Mapped to')
    dot.edge('logical_flows:f2', 'physical_resources:f2', label='Mapped to')

    # Edge to the callout box to show its relevance
    # Using constraint=false helps prevent this edge from affecting the main layout
    dot.edge('physical_resources', 'callout', style='dashed', arrowhead='none', constraint='false')

    # Render the graph to a file and open it automatically
    output_filename = 'abstraction_vs_reality_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_channel_mapping_diagram():
    """
    Creates and renders a diagram that visually explains the mapping from
    logical channels to physical resources via the MAC Scheduler.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('ChannelMappingRecap', comment='Channel Mapping Recap Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Top Layer: Logical Channels ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='Logical Layer (Functional Data Flows)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')
        c.attr('node', fillcolor='lightblue')
        # Define the logical channel nodes
        c.node('gse', 'GSE Logical Channel\n(User Traffic)')
        c.node('control', 'Control Logical Channel\n(Network Management)')
        c.node('signaling', 'Signaling Logical Channel\n(PLS, MODCOD Info)')
        # Use rank='same' to align them horizontally
        c.body.append('{ rank=same; gse; control; signaling }')

    # --- Middle Layer: MAC Scheduler ---
    dot.node('mac_scheduler', 'MAC Scheduler', shape='ellipse', fillcolor='white', style='filled')

    # --- Bottom Layer: Physical Layer Resources ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='Physical Layer Resources', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        # Define the physical resource nodes
        c.node('plframe', 'PLFRAME / BBFRAME')
        c.node('carrier', 'Carrier Frequency')
        c.node('modcod', 'MODCOD')
        # Use rank='same' to align them horizontally
        c.body.append('{ rank=same; plframe; carrier; modcod }')

    # --- Mapping Arrows ---
    # From Logical Channels to MAC Scheduler
    dot.edge('gse', 'mac_scheduler')
    dot.edge('control', 'mac_scheduler')
    dot.edge('signaling', 'mac_scheduler')

    # From MAC Scheduler to Physical Resources
    dot.edge('mac_scheduler', 'plframe', label='Maps to')
    dot.edge('mac_scheduler', 'carrier', label='Maps to')
    dot.edge('mac_scheduler', 'modcod', label='Maps to')

    # Render the graph to a file and open it automatically
    output_filename = 'channel_mapping_recap_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_rcs2_channel_mapping_diagram():
    """
    Creates and renders a diagram that visually explains the mapping from
    DVB-RCS2 logical channels to physical resources via the MAC Scheduler.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('RCS2_ChannelMapping', comment='DVB-RCS2 Channel Mapping Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Top Layer: Logical Channels ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='Logical Layer (Functional Data Flows)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')
        c.attr('node', fillcolor='lightblue')
        # Define the logical channel nodes
        c.node('tlc', 'Traffic Logical Channel (TLC)\n(User Payload)')
        c.node('clc', 'Control Logical Channel (CLC)\n(NCC Control Messages)')
        c.node('slc', 'Signaling Logical Channel (SLC)\n(Burst Timing & MODCOD Info)')
        # Use rank='same' to align them horizontally
        c.body.append('{ rank=same; tlc; clc; slc }')

    # --- Middle Layer: MAC Scheduler ---
    dot.node('mac_scheduler', 'MAC Scheduler', shape='ellipse', fillcolor='white', style='filled')

    # --- Bottom Layer: Physical Layer Resources ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='Physical Layer Resources', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        # Define the physical resource nodes
        c.node('mftdma', 'MF-TDMA Slots')
        c.node('burst', 'Burst Structure')
        c.node('carrier', 'Carrier Frequencies')
        # Use rank='same' to align them horizontally
        c.body.append('{ rank=same; mftdma; burst; carrier }')

    # --- Mapping Arrows ---
    # From Logical Channels to MAC Scheduler
    dot.edge('tlc', 'mac_scheduler')
    dot.edge('clc', 'mac_scheduler')
    dot.edge('slc', 'mac_scheduler')

    # From MAC Scheduler to Physical Resources
    dot.edge('mac_scheduler', 'mftdma', label='Maps to')
    dot.edge('mac_scheduler', 'burst', label='Maps to')
    dot.edge('mac_scheduler', 'carrier', label='Maps to')

    # Render the graph to a file and open it automatically
    output_filename = 'rcs2_channel_mapping_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_rcs2_channel_mapping_diagram():
    """
    Creates and renders a diagram that visually explains the mapping from
    DVB-RCS2 logical channels to physical resources via the MAC Scheduler.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('RCS2_ChannelMapping', comment='DVB-RCS2 Channel Mapping Diagram')
    dot.attr(rankdir='TB', splines='ortho', nodesep='1.0', ranksep='1.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Top Layer: Logical Channels ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='Logical Layer (Functional Data Flows)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')
        c.attr('node', fillcolor='lightblue')
        # Define the logical channel nodes
        c.node('tlc', 'Traffic Logical Channel (TLC)\n(User Payload)')
        c.node('clc', 'Control Logical Channel (CLC)\n(NCC Control Messages)')
        c.node('slc', 'Signaling Logical Channel (SLC)\n(Burst Timing & MODCOD Info)')
        # Use rank='same' to align them horizontally
        c.body.append('{ rank=same; tlc; clc; slc }')

    # --- Middle Layer: MAC Scheduler ---
    dot.node('mac_scheduler', 'MAC Scheduler', shape='ellipse', fillcolor='white', style='filled')

    # --- Bottom Layer: Physical Layer Resources ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='Physical Layer Resources', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        # Define the physical resource nodes
        c.node('mftdma', 'MF-TDMA Slots')
        c.node('burst', 'Burst Structure')
        c.node('carrier', 'Carrier Frequencies')
        # Use rank='same' to align them horizontally
        c.body.append('{ rank=same; mftdma; burst; carrier }')

    # --- Mapping Arrows ---
    # From Logical Channels to MAC Scheduler
    dot.edge('tlc', 'mac_scheduler')
    dot.edge('clc', 'mac_scheduler')
    dot.edge('slc', 'mac_scheduler')

    # From MAC Scheduler to Physical Resources
    dot.edge('mac_scheduler', 'mftdma', label='Maps to')
    dot.edge('mac_scheduler', 'burst', label='Maps to')
    dot.edge('mac_scheduler', 'carrier', label='Maps to')

    # Render the graph to a file and open it automatically
    output_filename = 'rcs2_channel_mapping_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_return_channel_mapping_diagram():
    """
    Creates and renders a diagram that visually explains the channel mapping
    process for the DVB-RCS2 return link (RCST to Gateway).
    """
    # Create a new directed graph
    dot = graphviz.Digraph('ReturnChannelMapping', comment='DVB-RCS2 Return Channel Mapping')
    dot.attr(rankdir='TB', splines='line', nodesep='0.8', ranksep='1.2')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- 1. Application/Network Layer at RCST ---
    dot.node('app_layer', '1. Application / Network Layer (at RCST)', fillcolor='lightgreen')

    # --- 2. Logical Channels ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='2. Logical Channels (DVB-RCS2)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='14')
        c.attr('node', fillcolor='lightgreen', shape='Mrecord')
        c.node('logical_channels',
               '{Traffic Logical Channel (TLC) | Control Logical Channel (CLC) | Signaling Logical Channel (SLC)}')

    # --- 3. MAC Scheduler ---
    dot.node('mac_scheduler', '3. MAC Scheduler (RCST + NCC Coordination)', shape='ellipse', fillcolor='white',
             style='filled')

    # --- 4. Physical Channels ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='4. Physical Channels (DVB-RCS2)', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='14')
        c.attr('node', fillcolor='lightgreen', shape='Mrecord')
        c.node('physical_channels',
               '{MF-TDMA Slots | Carrier Frequency | MODCOD}')

    # --- 5. Transmission ---
    dot.node('satellite', '5. Transmission via Satellite', shape='ellipse', fillcolor='lightyellow')
    dot.node('gateway', '6. Received by Gateway', fillcolor='lightblue')

    # --- Mapping and Transmission Arrows ---
    dot.edge('app_layer', 'logical_channels', label='Generates')
    dot.edge('logical_channels', 'mac_scheduler', label='Mapped by')
    dot.edge('mac_scheduler', 'physical_channels', label='Maps to')
    dot.edge('physical_channels', 'satellite')
    dot.edge('satellite', 'gateway')

    # Render the graph to a file and open it automatically
    output_filename = 'return_channel_mapping_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_channel_recap_diagram():
    """
    Creates and renders a final recap diagram showing the mapping from
    logical channels to physical resources for both DVB-S2X and DVB-RCS2.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('ChannelRecap', comment='Channel Recap Diagram')
    dot.attr(rankdir='LR', splines='ortho', nodesep='1.0', ranksep='2.5')
    dot.attr('node', shape='record', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Left Column: Logical Channels ---
    with dot.subgraph(name='cluster_logical') as c:
        c.attr(label='Logical Channels (Functional Data Flows)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')

        # DVB-RCS2 Logical Channels
        with c.subgraph(name='cluster_rcs2_logical') as rcs2:
            rcs2.attr(label='DVB-RCS2', style='rounded', color='white')
            rcs2.attr('node', fillcolor='lightgreen')
            rcs2.node('slc', '{Signaling Logical Channel (SLC) | Burst Timing}')
            rcs2.node('clc', '{Control Logical Channel (CLC) | NCC Control}')
            rcs2.node('tlc', '{Traffic Logical Channel (TLC) | User Payload}')

        # DVB-S2X Logical Channels
        with c.subgraph(name='cluster_s2x_logical') as s2x:
            s2x.attr(label='DVB-S2X', style='rounded', color='white')
            s2x.attr('node', fillcolor='lightblue')
            s2x.node('ctrl_s2x', '{Control Logical Channel | Network Mgmt}')
            s2x.node('sig_s2x', '{Signaling Logical Channel | PLS Code, MODCOD}')
            s2x.node('gse_lc', '{GSE Logical Channel | IP/MPEG-TS}')

    # --- Right Column: Physical Resources ---
    with dot.subgraph(name='cluster_physical') as c:
        c.attr(label='Channel Reality (What actually happens on air)', style='filled', color='lightgrey',
               fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightyellow', style='rounded,filled', shape='box')
        c.node('modcod', 'MODCOD')
        c.node('plframe', 'PLFRAME / BBFRAME')
        c.node('mftdma', 'MF-TDMA Slots')
        c.node('carrier', 'Carrier Frequencies')

    # --- Mapping Arrows ---
    # S2X Mappings
    dot.edge('sig_s2x', 'modcod')
    dot.edge('gse_lc', 'plframe')
    dot.edge('ctrl_s2x', 'plframe')

    # RCS2 Mappings
    dot.edge('tlc', 'mftdma')
    dot.edge('clc', 'mftdma')
    dot.edge('slc', 'carrier')

    # Render the graph to a file and open it automatically
    output_filename = 'channel_recap_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_ntn_nr_diagram():
    """
    Creates and renders a diagram that provides a high-level overview of
    a Non-Terrestrial Network (NTN) integrated with a 5G system.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('NTN_NR_Overview', comment='NTN NR Overview Diagram')
    dot.attr(rankdir='LR', splines='line', nodesep='1.5', ranksep='2.0')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Left Side: User Equipment ---
    # Using an HTML-like table to include the icon and text in the node.
    ue_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD><FONT POINT-SIZE="24">📱</FONT></TD></TR>
  <TR><TD>User Equipment (UE)</TD></TR>
</TABLE>>'''
    dot.node('ue', ue_label, shape='plain', fillcolor='lightgreen')

    # --- Middle: Satellite ---
    satellite_label = '''<
<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">
  <TR><TD><FONT POINT-SIZE="24">🛰️</FONT></TD></TR>
  <TR><TD>Satellite (GEO/MEO/LEO)</TD></TR>
</TABLE>>'''
    dot.node('satellite', satellite_label, shape='ellipse', style='rounded,filled', fillcolor='lightyellow')

    # --- Right Side: Ground Segment ---
    with dot.subgraph(name='cluster_ground') as c:
        c.attr(label='Ground Segment', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightblue')
        c.node('gateway', 'Gateway / NCC')
        c.node('5g_core', '5G Core')
        c.edge('gateway', '5g_core', label=' Connects to ')

    # --- Data Paths ---
    # To have labels on both sides of the arrows, we create two separate edges.
    dot.edge('ue', 'satellite', label=' NTN NR Uplink ', dir='both')
    dot.edge('satellite', 'gateway', label=' DVB-RCS2 Return ', dir='both')

    # Add labels for the reverse paths. Since graphviz doesn't easily support
    # two labels on a bidirectional edge, we can add them as separate graph labels
    # or use a more complex setup. For simplicity, we'll keep the main labels.
    # To better match the visual, we will use two directed edges.
    dot.edge('satellite', 'ue', label=' NTN NR Downlink ')
    dot.edge('gateway', 'satellite', label=' DVB-S2X Forward ')

    # Render the graph to a file and open it automatically
    output_filename = 'ntn_nr_overview_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")


def create_required_adaptations_diagram():
    """
    Creates and renders a diagram showing the required adaptations for
    NTN NR over DVB L1.
    """
    # Create a new directed graph
    dot = graphviz.Digraph('RequiredAdaptations', comment='Required Adaptations for NTN NR over DVB L1')
    dot.attr(rankdir='LR', splines='line', nodesep='1.0', ranksep='2.5')
    dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica')
    dot.attr('edge', fontname='Helvetica', fontsize='12')

    # --- Left Column: NTN NR Requirement ---
    with dot.subgraph(name='cluster_ntn') as c:
        c.attr(label='NTN NR Requirement', style='filled', color='lightgrey', fontname='Helvetica', fontsize='16')
        c.attr('node', fillcolor='lightblue')
        c.node('traffic', 'eMBB, mMTC, IoT traffic mix')
        c.node('beam', 'Dynamic beam switching')
        c.node('numerology', 'Flexible numerology')
        c.node('doppler', 'Doppler shifts (LEO/MEO)')
        c.node('rtt', 'Long RTT (> 500 ms GEO)')

    # --- Right Column: Required DVB L1 Adaptation ---
    with dot.subgraph(name='cluster_dvb') as c:
        c.attr(label='Required DVB L1 Adaptation', style='filled', color='lightgrey', fontname='Helvetica',
               fontsize='16')
        c.attr('node', fillcolor='lightgreen')
        c.node('modcod_qos', 'Adaptive MODCOD & QoS-aware allocation')
        c.node('sig_integ', 'Beam-specific signaling integration')
        c.node('slot_map', 'Subcarrier spacing alignment & slot mapping')
        c.node('freq_comp', 'Frequency pre-compensation & tracking')
        c.node('scheduling', 'Extended frame scheduling & HARQ timers')

    # --- Mapping Arrows ---
    dot.edge('traffic', 'modcod_qos')
    dot.edge('beam', 'sig_integ')
    dot.edge('numerology', 'slot_map')
    dot.edge('doppler', 'freq_comp')
    dot.edge('rtt', 'scheduling')

    # Render the graph to a file and open it automatically
    output_filename = 'required_adaptations_diagram'
    dot.render(output_filename, view=True, format='png', cleanup=True)

    print(f"Diagram '{output_filename}.png' is being displayed.")

# Run the function to create the diagram
if __name__ == "__main__":
    pass
