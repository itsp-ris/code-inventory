package game;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.GameMap;

public class TRex extends Dinosaur {
	private int age;

	/**
	 * Constructor.
	 * All young Velociraptors are represented by a 'r' and have 50 hit points.
	 * Young Velociraptors starting food level is 10 and their maximum food level is 50.
	 * 
	 * @param name	   The name of this TRex
	 * @param age	   The initial age of this TRex
	 */
	public TRex(String name, int age) {
		super(name, 'x', 50, 100, ActorSpecies.TREX, ActorClass.CARNIVORE, ActorClass.LANDBASED);
		setFoodLevel(10);
		super.followBehaviour = new FollowBehaviour();
		this.age = age;
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
		if (otherActor.toString().contains("Player")) {
			actions.add(new TagAction(this));
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
			//Change the Baby T-Rex's name to T-Rex when it becomes an adult
			super.name = "T-Rex";
			//Change the T-Rex's display character to 'R' when it becomes an adult
			super.displayChar = 'R';
			//Change the T-Rex's maximum hit points when it becomes an adult. All adult TRex has a maximum hit points of 100.
			super.maxHitPoints = 200;
			//Change the T-Rex's maximum food level when it becomes an adult. All adult TRex has a maximum food level of 100.
			super.maxFoodLevel = 200;
			//Add reproduce behavior to adult T-Rex
			super.addBehaviour(new ReproduceBehaviour());
		}
		
		return super.playTurn(actions, lastAction, map, display);
	}
}
