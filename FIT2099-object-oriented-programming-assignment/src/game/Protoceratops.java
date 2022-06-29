package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.GameMap;

/**
 * A herbivorous dinosaur.
 *
 */
public class Protoceratops extends Dinosaur {
	private int age;

	/** 
	 * Constructor.
	 * All Protoceratops are represented by a 'd' and have 50 hit points.
	 * Young Protoceratops starting food level is 10 and their maximum food level is 50.
	 * 
	 * @param name	   	  The name of this Protoceratops
	 * @param age		  the initial age of the dinosaur
	 */
	public Protoceratops(String name, int age) {
		super(name, 'p', 50, 25, ActorSpecies.PROTOCERATOPS, ActorClass.HERBIVORE, ActorClass.LANDBASED);
		setFoodLevel(10);
		this.age = age;
		ActorSpecies.VELOCIRAPTORS.addTarget(this);
		ActorSpecies.TREX.addTarget(this);
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
			if (otherActor.toString().contains("Player")) {
				actions.add(new TagAction(this));
			}
		}
		return actions;
	}
	
	/**
	 * Select and return an action to perform on the current turn. 
	 *
	 * @param actions    Collection of possible Actions for this Dinosaur
	 * @param lastAction The Action this Actor took last turn. Can do interesting things in conjunction with Action.getNextAction()
	 * @param map        The map containing the Actor
	 * @param display    The I/O object to which messages may be written
	 * @return the Action to be performed
	 */
	@Override
	public Action playTurn(Actions actions, Action lastAction, GameMap map, Display display) {
		//Counter to determine change of growth phase
		age+=1;
		
		if (age == 30) {
			//Change the Baby Protoceratop's name to Protoceratops when it becomes an adult
			super.name = "Protoceratops";
			//Change the Protoceratop's display character to 'p' when it becomes an adult
			super.displayChar = 'd';
			//Change the Protoceratop's maximum hit points when it becomes an adult. All adult Protoceratops has a maximum hit points of 100.
			super.maxHitPoints = 100;
			//Change the Protoceratop's maximum food level when it becomes an adult. All adult Protoceratops has a maximum food level of 100.
			super.maxFoodLevel = 50;
			//Add reproduce behavior to adult Protoceratops
			super.addBehaviour(new ReproduceBehaviour());
		}
		
		return super.playTurn(actions, lastAction, map, display);
	}
}
