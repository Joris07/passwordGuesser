# Programmation Orientée Objet

Ce projet met en œuvre les principes de la Programmation Orientée Objet (POO) dans le langage de programmation Python.

## Polymorphisme

[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Capitalize.py#L7)

Le polymorphisme est la capacité d'un objet à prendre différentes formes et à se comporter de différentes manières en fonction du contexte. En POO, le polymorphisme permet à des objets de classes différentes d'être traités de manière uniforme à travers une interface commune, mais avec des comportements spécifiques à chaque classe.

## Encapsulation

[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Possibilites.py#L13)

L'encapsulation est un principe de la POO qui consiste à regrouper les données (attributs) et les méthodes qui les manipulent en une seule entité, appelée classe. L'encapsulation permet de cacher les détails internes de la classe et de contrôler l'accès aux données en utilisant des méthodes publiques.

- L'encapsulation publique permet un accès direct aux attributs et méthodes de la classe. 
[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Characters.py#L9)
- L'encapsulation protégée limite l'accès aux attributs et méthodes à la classe elle-même et à ses sous-classes. 
[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Words.py#L6)
- L'encapsulation privée restreint l'accès aux attributs et méthodes uniquement à l'intérieur de la classe elle-même. 
[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Date.py#L5)

## Composition

[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Engine.py#L26)

La composition est un concept de la POO qui permet à une classe d'être composée d'objets d'autres classes. Cela signifie qu'une classe peut contenir des instances d'autres classes en tant qu'attributs. La composition permet de créer des relations complexes entre les objets en les combinant de manière flexible.

## Héritage

[Lien vers le parent :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Possibilites.py#L3)

[Lien vers l'enfant :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Words.py#L3)

L'héritage est un mécanisme de la POO qui permet à une classe de hériter les attributs et les méthodes d'une autre classe, appelée classe parent ou superclasse. La classe qui hérite est appelée classe enfant ou sous-classe. L'héritage permet de créer une hiérarchie de classes et de partager du code commun tout en permettant aux classes dérivées d'ajouter ou de modifier le comportement hérité.

## Interface

[Lien vers le code :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Possibilites.py#L8)

Une interface en POO est une spécification d'un ensemble de méthodes qu'une classe doit implémenter. Elle définit le contrat que toute classe implémentant cette interface doit respecter. En Python, il n'y a pas de construction spécifique pour les interfaces, mais il est possible de créer des classes abstraites qui servent de base pour les classes concrètes.

Une classe abstraite peut définir des méthodes abstraites, qui sont des méthodes sans implémentation. Les classes qui héritent de cette classe abstraite doivent fournir une implémentation concrète pour ces méthodes abstraites. Cela permet de créer des contrats ou des spécifications pour les classes dérivées, qui doivent respecter l'interface définie par la classe abstraite.

## Méthodes et attributs d'objets

[Lien vers méthode d'objet :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Engine.py#L20) 

[Lien vers attribut d'objet :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Possibilites.py#L6)

Les méthodes et les attributs d'objets sont des membres d'une classe qui sont accessibles à partir des instances de cette classe. Les méthodes sont des fonctions spécifiques à une classe, tandis que les attributs sont des variables associées à une instance de la classe.

## Méthodes et attributs statiques

[Lien vers méthode statique :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Config.py#L99)

[Lien vers attribut statique :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Config.py#L2)

Les méthodes et les attributs statiques sont des membres d'une classe qui appartiennent à la classe elle-même plutôt qu'à ses instances. Ils sont accessibles directement à partir de la classe, sans avoir besoin d'instancier un objet. Les méthodes statiques sont des fonctions liées à une classe, tandis que les attributs statiques sont des variables partagées par toutes les instances de la classe.

## Méthodes et attributs de classe

[Lien vers méthode de classe :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Characters.py#L13)

[Lien vers attribut de classe :](https://github.com/Joris07/passwordGuesser/blob/cea37104cf9bf9b6c8643ef3d5c0e17722058888/Classes/Options/Characters.py#L6)

Les méthodes et les attributs de classe sont des membres d'une classe qui sont associés à la classe elle-même, plutôt qu'à ses instances ou à ses sous-classes. Ils sont accessibles à partir de la classe et peuvent être partagés par toutes les instances de la classe. Les méthodes de classe sont des fonctions qui opèrent sur la classe elle-même plutôt que sur les instances, tandis que les attributs de classe sont des variables partagées par toutes les instances de la classe.