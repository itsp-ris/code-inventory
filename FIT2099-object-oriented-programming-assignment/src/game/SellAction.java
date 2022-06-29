package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.interfaces.ItemInterface;

/**
 * Special Action for selling Items to Shop.
 */
public class SellAction extends Action {
	private ItemInterface item;
	
	/**
	 * Constructor.
	 * @param item the Item to sell
	 */
	public SellAction(ItemInterface item) {
		this.item = item;
	}
	
	/**
	 * Sell the Item.
	 * @param actor The Actor performing the Action
	 * @param map 	The map the Actor is on
	 * @return a description of the Action suitable for feedback in the UI
	 */
	@Override
	public String execute(Actor actor, GameMap map) {
		String result;
		
		actor.removeItemFromInventory((Item) item);
		
		double itemCost = item.getCost();
		((Player) actor).setCash(itemCost);
		
		result = actor + " earns " + itemCost;
		return result;
	}
	
	/**
	 * A string describing the Action suitable for displaying in the UI menu.
	 * @param actor The actor performing the action.
	 * @return a String, e.g. "Player drops the potato"
	 */
	@Override
	public String menuDescription(Actor actor) {
		return actor + " sells " + item.toString();
	}

}
