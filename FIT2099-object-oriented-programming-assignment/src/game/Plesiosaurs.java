package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.GameMap;

public class Plesiosaurs extends Dinosaur {
	private int age;
	
	/**
	 * Constructor.
	 * All young Plesiosaurs are represented by a '2' and have 50 hit points.
	 * Young Plesiosaurs starting food level is 10 and their maximum food level is 50.
	 * 
	 * @param name	   The name of this Plesiosaurs
	 */
	public Plesiosaurs(String name, int age) {
		super(name, '2', 50, 50, ActorSpecies.PLESIOSAURS, ActorClass.CARNIVORE, ActorClass.WATERBASED);
		setFoodLevel(10);
		super.followBehaviour = new FollowBehaviour();
		this.age = age;
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
		if (otherActor.getActorClass() != ActorClass.HERBIVORE && otherActor.getSpecies() != ActorSpecies.PLESIOSAURS) {
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
			//Change the Baby Plesiosaurs' name to Plesiosaurs when it becomes an adult
			super.name = "Plesiosaurs";
			//Change the Plesiosaurs' display character to 'P' when it becomes an adult
			super.displayChar = 'P';
			//Change the Plesiosaurs' maximum hit points when it becomes an adult. All adult Plesiosaurs has a maximum hit points of 150.
			super.maxHitPoints = 150;
			//Change the Plesiosaurs' maximum food level when it becomes an adult. All adult Plesiosaurs has a maximum food level of 100.
			super.maxFoodLevel = 100;
			//Add reproduce behavior to adult Plesiosaurs
			super.addBehaviour(new ReproduceBehaviour());
		}
		
		return super.playTurn(actions, lastAction, map, display);
	}
}
