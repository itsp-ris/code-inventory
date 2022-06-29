package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.interfaces.ItemInterface;

/**
 * Special Action for buying Items from Shop.
 */
public class BuyAction extends Action {
	private ItemInterface item;
	
	/**
	 * Constructor.
	 * @param item the Item to buy
	 */
	public BuyAction(ItemInterface item) {
		this.item = item;
	}
	
	/**
	 * Buy the Item.
	 * @param actor The Actor performing the Action
	 * @param map 	The map the Actor is on
	 * @return a description of the Action suitable for feedback in the UI
	 */
	@Override
	public String execute(Actor actor, GameMap map) {
		String result;
		
		double itemPrice = item.getPrice();
		if (itemPrice < ((Player) actor).getCash()) {
			((Player) actor).setCash(-itemPrice);
			actor.addItemToInventory((Item) item);
			result = item.toString() + " added to " + actor + "'s inventory";
		} else {
			result = actor + " "+ "does not have enough cash.";
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
		return actor + " buys " + item.toString();
	}

}
