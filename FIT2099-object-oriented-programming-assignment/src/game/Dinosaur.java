package game;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

import edu.monash.fit2099.engine.Action;
import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Display;
import edu.monash.fit2099.engine.GameMap;

/**
 * Class representing the Dinosaurs.
 */
public abstract class Dinosaur extends Actor {
	private Random rand = new Random();
	//The dinosaur has a feed behaviour but is not added to the list of behaviours for immediate access in playTurn method
	private Behaviour feedBehaviour = new FeedBehaviour();
	//The dinosaur has a search food behaviour but is not added to the list of behaviours for immediate access in playTurn method
	private Behaviour searchFoodBehaviour = new SearchFoodBehaviour();
	//The dinosaur has a follow behaviour but is not added to the list of behaviours for immediate access in playTurn method
	protected Behaviour followBehaviour;
	
	//Each species and growth stage has a different starting food level, hence, the variable will be initialize upon creation of Dinosaurs
	private int foodLevel;
	/**
	 * The Dinosaur's maximum food level
	 */
	//Each species and growth stage has a different maximum food level, hence, the variable will be initialize upon creation of Dinosaurs
	protected int maxFoodLevel;
	
	private ActorSpecies species;
	private ActorClass actorClass;
	private ActorClass actorEco;
	
	/**
	 * Constructor.
	 * @param name		   The name of the Dinosaur
	 * @param displayChar  The character that will represent the Dinosaur in the display
	 * @param hitPoints	   The Dinosaur's starting hit points
	 * @param maxFoodLevel The Dinosaur's maximum food level
	 * @param species	   The type of Dinosaur
	 * @param actorClass   The category of the Dinosaur
	 * @param actorEco	   The habitat category of the Dinosaur
	 */
	public Dinosaur(String name, char displayChar, int hitPoints, int maxFoodLevel, ActorSpecies species, ActorClass actorClass, ActorClass actorEco) {
		super(name, displayChar, hitPoints);
		this.maxFoodLevel = maxFoodLevel;
		this.species = species;
		this.actorClass = actorClass;
		this.actorEco = actorEco;
		addBehaviour(new WanderBehaviour());
	}
	
	private List<Behaviour> behaviours = new ArrayList<Behaviour>();
	
	/**
	 * Add a behaviour to this Dinosaur's implemented list of behaviors.
	 * @param behaviour The Behaviour to add
	 */
	public void addBehaviour(Behaviour behaviour) {
		behaviours.add(0, behaviour);
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
		//The Dinosaur's food level decrease by one in each turn
		setFoodLevel(-1);
		
		//Returns Action in corresponds to being hungry
		if (foodLevel < maxFoodLevel*0.5) {
			int x = map.locationOf(this).x();
			int y = map.locationOf(this).y();
			display.println(this + " at " + "(" + x + "," + " " + y + ")" + " " + "is hungry!");
			//Feed on food/egg(s) at the Dinosaur's current location, if there is
			Action feed = feedBehaviour.getAction(this, map);
			if (feed != null) {
				return feed;
			}
			
			if (followBehaviour != null) {
				Action follow = followBehaviour.getAction(this, map);
				//Follow Actor to feed on, if there is
				if (follow != null) {
					return follow;
				}
			}
			
			Action search = searchFoodBehaviour.getAction(this, map);
			//Search for grass/tree/food/egg(s) to feed on, if there is
			if (search != null) {
				return search;
			}
		}
		
		//Returns Action in corresponds to not being hungry
		if (foodLevel >= maxFoodLevel*0.4) {
			//Performs Action of a behaviour
			for (Behaviour behaviour : behaviours) {
				Action action = behaviour.getAction(this, map);
				if (action != null) {
					return action;
				}
			}
		}
		
		//Attack Actor at the Dinosaur's adjacent Exit to e.g.: feed on, if there is
		for (Action action : actions) {
			if (action instanceof AttackAction) {
				return action;
			}
		}
		
		return actions.get(rand.nextInt(actions.size()));
	}
	
	/**
	 * Returns a collection of the Actions that the otherActor can do to the current Actor.
	 *
	 * @param otherActor the Actor that might be performing attack
	 * @param direction  String representing the direction of the other Actor
	 * @param map        current GameMap
	 * @return A collection of Actions.
	 */
	public Actions getAllowableActions(Actor otherActor, String direction, GameMap map) {
		Actions actions = super.getAllowableActions(otherActor, direction, map);
		
		if (otherActor instanceof Player) {
			actions.add(new TagAction(this));
		}
		
		return actions;
	}
	
	/**
	 * Set the current food level after a turn or an action following feed behaviour.
	 * @param nutrients the amount of nutrients lost or consumed
	 */
	public void setFoodLevel(int nutrients) {
		foodLevel += nutrients;
		if (foodLevel > maxFoodLevel) {
			foodLevel = maxFoodLevel;
		}
		
		if (foodLevel <= 0) {
			super.hurt(hitPoints);
		}
	}
	
	/**
	 * Accessor for the Dinosaur's species.
	 * @return the Dinosaur's species
	 */
	@Override
	public ActorSpecies getSpecies() {
		return species;
	}

	/**
	 * Accessor for the Dinosaur's category.
	 * @return the Dinosaur's category
	 */
	@Override
	public ActorClass getActorClass() {
		return actorClass;
	}
	
	/**
	 * Accessor for the Dinosaur's habitat category.
	 * @return the Dinosaur's habitat category
	 */
	@Override
	public ActorClass getActorEco() {
		return actorEco;
	}
}
