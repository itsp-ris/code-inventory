package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.interfaces.FoodInterface;

/**
 * Class representing a Dinosaur's characteristic
 */
public class FeedBehaviour implements Behaviour {
	
	/**
	 * Returns a FeedAction to feed on the food/egg(s) at the Dinosaur's current location, if possible.  
	 * If no feeding is possible, returns null.
	 * 
	 * @param actor The Dinosaur enacting the behaviour
	 * @param map 	The map that Dinosaur is currently on
	 * @return an Action, or null if no FeedAction is possible
	 */
	@Override
	public Action getAction(Actor actor, GameMap map) {
		Location here = map.locationOf(actor);
		
		for (Item item:here.getItems()) {
			if (item instanceof FoodInterface) {
				return new FeedAction((FoodInterface) item);
			}
		}
		
		return null;
	}
}
