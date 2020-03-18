from enum import Enum
from collections import namedtuple


Type = Enum("Type", ("CURE", "HEALTHY", "SICK", "DYING", "DEAD"))
Agent = namedtuple("Agent", ("name", "category"))

def meetup(agent_listing: tuple) -> list:
    """Model the outcome of the meetings of pairs of agents.

    The pairs of agents are ((a[0], a[1]), (a[2], a[3]), ...). If there's an uneven
    number of agents, the last agent will remain the same.

    Notes
    -----
    The rules governing the meetings were described in the question. The outgoing
    listing may change its internal ordering relative to the incoming one.

    Parameters
    ----------
    agent_listing : tuple of Agent
        A listing (tuple in this case) in which each element is of the Agent
        type, containing a 'name' field and a 'category' field, with 'category' being
        of the type Type.

    Returns
    -------
    updated_listing : list
        A list of Agents with their 'category' field changed according to the result
        of the meeting.
    """
    meeting = []
    new_agents=[]
    agent_listing=list(agent_listing)
    to_remove=[]
    for i in agent_listing:
        if i[1]== Type.DEAD or i[1]== Type.HEALTHY:
            new_agents.append(i)
            to_remove.append(i)
    for m in to_remove:
        agent_listing.remove(m)
    if len(agent_listing)%2==0:
        for i in range(0, len(agent_listing),2):
            meeting=meeting+[(agent_listing[i], agent_listing[i+1])]
    else:
        for j in range(0,len(agent_listing)-1,2):
            meeting=meeting+[(agent_listing[j], agent_listing[j+1])]
        new_agents.append(agent_listing[-1])
    for meet in meeting:
        bool = True
        if meet[0][1] ==Type.DYING and meet[1][1] ==Type.DYING:
            new_agents.append(Agent(meet[0][0], Type.DEAD))
            new_agents.append(Agent(meet[1][0], Type.DEAD))
            bool=False
        if meet[0][1] == Type.DYING and meet[1][1] == Type.SICK:
            new_agents.append(Agent(meet[0][0], Type.DEAD))
            new_agents.append(Agent(meet[1][0], Type.DYING))
            bool = False
        if meet[0][1] ==Type.SICK and meet[1][1] ==Type.DYING:
            new_agents.append(Agent(meet[0][0], Type.DYING))
            new_agents.append(Agent(meet[1][0], Type.DEAD))
            bool = False
        if meet[0][1] ==Type.CURE and meet[1][1] ==Type.SICK:
            new_agents.append(Agent(meet[0][0], Type.CURE))
            new_agents.append(Agent(meet[1][0], Type.HEALTHY))
            bool = False
        if meet[0][1] ==Type.CURE and meet[1][1] ==Type.DYING:
            new_agents.append(Agent(meet[0][0], Type.CURE))
            new_agents.append(Agent(meet[1][0], Type.SICK))
            bool = False
        if meet[0][1] ==Type.SICK and meet[1][1] ==Type.CURE:
            new_agents.append(Agent(meet[0][0], Type.HEALTHY))
            new_agents.append(Agent(meet[1][0], Type.CURE))
            bool = False
        if meet[0][1] ==Type.DYING and meet[1][1] ==Type.CURE:
            new_agents.append(Agent(meet[0][0], Type.SICK))
            new_agents.append(Agent(meet[1][0], Type.CURE))
            bool = False
        if meet[0][1] ==Type.SICK and meet[1][1] ==Type.SICK:
            new_agents.append(Agent(meet[0][0], Type.DYING))
            new_agents.append(Agent(meet[1][0], Type.DYING))
            bool = False
        if bool:
            new_agents.append(Agent(meet[0][0], meet[0][1]))
            new_agents.append(Agent(meet[1][0], meet[1][1]))

    return (new_agents)

