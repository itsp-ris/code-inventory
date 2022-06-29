package game;

import java.util.List;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Exit;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.engine.MoveActorAction;

/**
 * A class that figures out a MoveAction that will move the Actor one step 
 * closer to a Food supply.
 */
public class SearchFoodBehaviour implements Behaviour {
	
	/**
	 * Returns a MoveAction to move the Actor one step closer to a food supply, if possible.  
	 * If no movement is possible, returns null.
	 * 
	 * @param actor The Actor enacting the behaviour
	 * @param map 	The map that Actor is currently on
	 * @return an Action, or null if no MoveAction is possible
	 */
	@Override
	public Action getAction(Actor actor, GameMap map) {
		Location here = map.locationOf(actor);
		List<Location> food = actor.getActorClass().getFoodSource();
		
		if (food.size() != 0) {
			Location there = food.get(0);
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
