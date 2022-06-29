package game;

import java.util.List;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.DropItemAction;
import edu.monash.fit2099.engine.GameMap;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Menu;

/**
 * Class representing the Player.
 */
public class Player extends Actor {

	private Menu menu = new Menu();
	private double cashBalance = 1000;

	/**
	 * Constructor.
	 *
	 * @param name        Name to call the player in the UI
	 * @param displayChar Character to represent the player in the UI
	 * @param hitPoints   Player's starting number of hitpoints
	 */
	public Player(String name, char displayChar, int hitPoints) {
		super(name, displayChar, hitPoints);
	}
	
	/**
	 * Returns a collection of the Actions that the otherActor can do to the current Actor.
	 *
	 * @param otherActor the Actor that might be performing attack
	 * @param direction  String representing the direction of the other Actor
	 * @param map        current GameMap
	 * @return A collection of Actions.
	 */
	@Override
	public Actions getAllowableActions(Actor otherActor, String direction, GameMap map) {
		Actions actions = super.getAllowableActions(otherActor, direction, map);
		if (otherActor.getActorClass() != ActorClass.HERBIVORE) {
			actions.add(new AttackAction(this));
		}
		return actions;
	}
	
	/**
	 * Select and return an action to perform on the current turn. 
	 *
	 * @param actions    Collection of possible Actions for this Actor
	 * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
	 * @param map        The map containing the Actor
	 * @param display    The I/O object to which messages may be written
	 * @return the Action to be performed
	 */
	@Override
	public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display) {
		actions.add(new QuitAction());
		
		// Handle multi-turn Actions
		if (lastAction.getNextAction() != null)
			return lastAction.getNextAction();
		Action action = menu.showMenu(this, actions, display);
		
		List<Item> inventory = this.getInventory();
		for (Item item : inventory) {
			if (item.toString().contains("egg")) {
				if (((Egg) item).getAge() >= 18) { 
					if (((Egg) item).getActorEco() != ActorClass.WATERBASED) {
						display.println(item.toString() + " " + "is ready to hatch! Please drop it");
					} else {
						display.println(item.toString() + " " + "is ready to hatch! Please drop it near water");
					}
				}
			}
		}
		
		return action;
	}
	
	/**
	 * Setter to update the amount of cash after e.g.: buying and selling action.
	 * @param amount the amount received or used
	 */
	public void setCash(double amount) {
		cashBalance += amount;
	}
	
	/**
	 * Accessor for the amount of money in possession
	 * @return the amount money possessed
	 */
	public double getCash() {
		return cashBalance;
	}
	
	/**
	 * Accessor for the Actor's species.
	 * @return the Actor's species
	 */
	@Override
	public ActorSpecies getSpecies() {
		return ActorSpecies.HUMANS;
	}
	
	/**
	 * Accessor for the Actor's category.
	 * @return the Actor's category
	 */
	@Override
	public ActorClass getActorClass() {
		return ActorClass.OMNIVORE;
	}
	
	/**
	 * Accessor for the Actor's habitat category.
	 * @return the Actor's habitat category
	 */
	@Override
	public ActorClass getActorEco() {
		return ActorClass.LANDBASED;
	}
}
