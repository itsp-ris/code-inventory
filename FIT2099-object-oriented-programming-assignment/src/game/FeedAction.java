package game;

import edu.monash.fit2099.demo.conwayslife.Status;
import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.interfaces.FoodInterface;

/**
 * Special Action for feeding on Items at the Actor's location.
 */
public class FeedAction extends Action {
	private FoodInterface food;

	/**
	 * Constructor.
	 * @param item The Item to feed on
	 */
	public FeedAction(FoodInterface item) {
		this.food = item;
	}
	
	/**
	 * Feed on the Item.
	 * @param actor The Actor performing the Action
	 * @param map 	The map the Actor is on
	 * @return a description of the Action suitable for feedback in the UI
	 */
	@Override
	public String execute(Actor actor, GameMap map) {
		String result;
		((Dinosaur) actor).setFoodLevel(food.getNutrients());
		
		food.setStatus(Status.EATEN);
		actor.getActorClass().removeFoodSource(map.locationOf(actor));
		
		result = actor + " ate " + food.toString();
		return result;
	}
	
	/**
	 * A string describing the Action suitable for displaying in the UI menu.
	 * @param actor The actor performing the action.
	 * @return a String, e.g. "Player drops the potato"
	 */
	@Override
	public String menuDescription(Actor actor) {
		return actor + " eats " + food.toString();
	}
}
