package game;

import java.util.ArrayList;
import java.util.List;

import edu.monash.fit2099.engine.*;

/**
 * A class that figures out a MoveAction that will move the Actor one step 
 * closer to a target Actor.
 */
public class FollowBehaviour implements Behaviour {

	/**
	 * Returns a MoveAction to move the Actor one step closer to a target Actor, if possible.  
	 * If no movement is possible, returns null.
	 * 
	 * @param actor The Actor enacting the behaviour
	 * @param map 	The map that Actor is currently on
	 * @return an Action, or null if no MoveAction is possible
	 */
	@Override
	public Action getAction(Actor actor, GameMap map) {
		Location here = map.locationOf(actor);
		List<Actor> targets = actor.getSpecies().getTarget();
		
		for (Actor target : targets) {
			if (map.locationOf(target) != null) {
				Location there = map.locationOf(target);
				int currentDistance = distance(here, there);
				for (Exit exit : here.getExits()) {
					Location destination = exit.getDestination();
					if (destination.canActorEnter(actor)) {
						int newDistance = distance(destination, there);
						if (newDistance < currentDistance) {
							return new MoveActorAction(destination, exit.getName());
						}
					}
				}
			}
		}

		return null;
	}

	/**
	 * Compute the Manhattan distance between two locations.
	 * 
	 * @param a the first location
	 * @param b the first location
	 * @return the number of steps between a and b if you only move in the four cardinal directions.
	 */
	private int distance(Location a, Location b) {
		return Math.abs(a.x() - b.x()) + Math.abs(a.y() - b.y());
	}
}