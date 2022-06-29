/**
 * 
 */
package game;

import java.util.List;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;

public class TagAction extends Action {
	private Actor target;
	
	/**
	 * Constructor.
	 * @param target The Actor to tag
	 */
	public TagAction(Actor target) {
		this.target = target;
	}
	
	/**
	 * Tag the Actor.
	 * @param actor The Actor performing the Action
	 * @param map 	The map the Actor is on
	 * @return a description of the Action suitable for feedback in the UI
	 */
	@Override
	public String execute(Actor actor, GameMap map) {
		String result = actor + " " + "does not have Dinosaur Tag in inventory";
		
		List<Item> inventory = actor.getInventory();
		
		for (Item item : inventory) {
			if (item.toString().equals("Dinosaur Tag")) {
				actor.removeItemFromInventory(item);
				
				ActorSpecies targetSpecies = ((Dinosaur) target).getSpecies();
				double targetCost = targetSpecies.getActorCost();
				((Player) actor).setCash(targetCost);
				map.removeActor(target);
				
				result = actor + " earns " + targetCost;
				return result;
			}
		}
		
		return result;
	}
	
	/**
	 * A string describing the Action suitable for displaying in the UI menu.
	 * @param actor The actor performing the action.
	 * @return a String, e.g. "Player drops the potato"
	 */
	@Override
	public String menuDescription(Actor actor) {
		return actor + " tags " + target;
	}

}
