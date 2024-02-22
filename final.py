import numpy as np
import matplotlib.pyplot as plt
import math
from numpy.core.fromnumeric import mean

from numpy.lib.npyio import genfromtxt 

#FUNCTION DECLARATIONS:
def is_valid_choice(option):
    """A function that checks if the menu choice entered is valid or not

        Parameters: option (str object)
        Return: True, False

    """
    if option not in [1,2,3]:
        print('INVALID CHOICE! \n')
        print('Please enter your country name again and enter a valid choice between (1-3).\n')
        return False

    else:
        return True


def is_year_Valid(year_option):
    """A function that checks if the year entered for displaying population data was accurate or not

        Parameters: year_option (str object)
        Return: True, False

    """

    if int(year_option)<2000 or int(year_option)>2020:
        print('INVALID YEAR SELECTION!\n')
        print('Please enter your country name and choice again along with a valid year choice (2000-2020).\n')
        return False

    else:
        return True




#CLASS DECLARATION:
class NationInfo:
    """
    
    A class used to create a NatoinInfo object

    Attributes:
        country (str): String that represents the country name
        region (str): String that represents the UN Region name


    
    """

    def __init__(self, name, region, sub_region, area):
        self.name = name
        self.region = region
        self.sub_region = sub_region
        self.area = area
        
    
    def print_nation_info(self):
        """
        
        A function that prints information about a particular country such as its UN designated region and sub_region as well as its area in square
        kilometers.

        Parameters: None
        Return: None

        """
        print(f"Country: {self.name} | UN Designated Region: {self.region} | UN Designated Sub-Region: {self.sub_region} | Area of the country: {self.area} sq. km\n\n")



#MAIN BODY OF CODE: 
def main():

    #IMPORTING DATA FROM THE .CSV FILES INTO NUMPY ARRAYS:
    Country_Data = np.genfromtxt('Country_Data.csv', delimiter = ',', skip_header = True, encoding= None, dtype = np.dtype([('Country','U20'), ('Region', 'U20'), ('SubRegion', 'U20'), ('Area', 'i4')]))
    Population_Data = np.genfromtxt('Population_Data.csv', delimiter = ',', skip_header = True, encoding= None, dtype = np.dtype([('Country', 'U20'), ('2000_Pop', 'i8'), ('2001_Pop', 'i8'), ('2002_Pop', 'i8') , ('2003_Pop', 'i8') , ('2004_Pop', 'i8') , ('2005_Pop', 'i8') , ('2006_Pop', 'i8') , ('2007_Pop', 'i8') , ('2008_Pop', 'i8') , ('2009_Pop', 'i8') , ('2010_Pop', 'i8') , ('2011_Pop', 'i8') , ('2012_Pop', 'i8') , ('2013_Pop', 'i8') , ('2014_Pop', 'i8') , ('2015_Pop', 'i8') , ('2016_Pop', 'i8'), ('2017_Pop', 'i8') , ('2018_Pop', 'i8') , ('2019_Pop', 'i8') , ('2020_Pop', 'i8')]))
    Threatened_Species_Data = np.genfromtxt('Threatened_Species.csv', delimiter = ',', skip_header = True, encoding= None, dtype = np.dtype([('Country', 'U20'), ('Plants', 'i2'), ('Fish', 'i2'), ('Birds', 'i2'), ('Mammals', 'i2')]))

    #NUMPY ARRAYS AS DICTIONARIES & LISTS:
    Countries_list = list(Country_Data['Country'])

    Num_of_Countries = len(Countries_list)

    print('---------------------------COUNTRY STATISTICS PROGRAM:------------------------------\n')
    flag = True

    while flag == True:
        User_input = input('Enter the name of the country (enter x to exit the program): ')

        if User_input == 'x':
            exit()

        User_Country = NationInfo('a','a','a','a')
        
        #Checks if the users input is a valid country name
        if User_input in Countries_list:
            User_Country.name = User_input

        else: #If the country name entered is not valid then it asks the user again
            print('Enter a valid country name')
            continue


        #Getting the rest of the data of the country:
        for i in range(Num_of_Countries):
            if User_Country.name == Country_Data['Country'][i] and User_Country.name == Population_Data['Country'][i]:
                User_Country.region = Country_Data['Region'][i]
                User_Country.sub_region = Country_Data['SubRegion'][i]
                User_Country.area = Country_Data['Area'][i]
                
        

        #Asking the user what information they want about the country:
        print(f'You chose the country of {User_Country.name}.')
        print('What information of the selected country would you like to see? (Choose from the following options):\n')

        print('1.) The region and sub-region in which the country is located\n')

        print('2.) Population data of the country and for its corresponding sub-region and region\n')
        
        print('3.) Data for threatened species in the country and for its corresponding sub-region and region\n')
        

        #User chooses they'd like to see:
        choice = int(input('Enter your choice (1-3) from the options above based on the information you would like to see: '))
        print(f'You have chosen option {choice}\n\n')

        #Check if the choice is valid:
        if is_valid_choice(choice) == False:
            continue

        else:
            pass

            
        


        if choice == 1:
        ######################################## LOCATION DATA FOR THE COUNTRY #############################################################
            print(f'################ REGION AND SUB-REGION OF {User_Country.name}: #################')
            User_Country.print_nation_info() #calls the class method 







        elif choice == 2:
        ########################################### POPULATION DATA FOR THE COUNTRY #######################################################
        
            print(f'############################################  POPULATION DATA OF {User_Country.name}:  #####################################')

            #Getting the population data for the country on a yearly basis:
            for i in range(Num_of_Countries):
                if User_Country.name == Population_Data['Country'][i]:
                    pop_2000 = Population_Data['2000_Pop'][i]
                    pop_2001 = Population_Data['2001_Pop'][i]
                    pop_2002 = Population_Data['2002_Pop'][i]
                    pop_2003 = Population_Data['2003_Pop'][i]
                    pop_2004 = Population_Data['2004_Pop'][i]
                    pop_2005 = Population_Data['2005_Pop'][i]
                    pop_2006 = Population_Data['2006_Pop'][i]
                    pop_2007 = Population_Data['2007_Pop'][i]
                    pop_2008 = Population_Data['2008_Pop'][i]
                    pop_2009 = Population_Data['2009_Pop'][i]
                    pop_2010 = Population_Data['2010_Pop'][i]
                    pop_2011 = Population_Data['2011_Pop'][i]
                    pop_2012 = Population_Data['2012_Pop'][i]
                    pop_2013 = Population_Data['2013_Pop'][i]
                    pop_2014 = Population_Data['2014_Pop'][i]
                    pop_2015 = Population_Data['2015_Pop'][i]
                    pop_2016 = Population_Data['2016_Pop'][i]
                    pop_2017 = Population_Data['2017_Pop'][i]
                    pop_2018 = Population_Data['2018_Pop'][i]
                    pop_2019 = Population_Data['2019_Pop'][i]
                    pop_2020 = Population_Data['2020_Pop'][i]
            
            #Compiling the Data into lists and arrays for plotting and manipulation:
            Country_Populations_List = [pop_2000, pop_2001, pop_2002, pop_2003, pop_2004, pop_2005, pop_2006, pop_2007, pop_2008, pop_2009, pop_2010, pop_2011, pop_2012, pop_2013, pop_2014, pop_2015, pop_2016, pop_2017, pop_2018, pop_2019, pop_2020]
            Country_Populations_Array = np.array(Country_Populations_List)
            Years_Array = np.array([2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020])

            #Population Statistics:

            #Population of the country each year since 2000-2020  
            print(f'Population data for {User_Country.name}') 

            for i in range(21):     
                print('Year:     Population:')                     
                print(Years_Array[i], '    ', Country_Populations_List[i],'\n')

            #Average population of the country over the past two decades (2000-2020):
            Avg_Num_of_Ppl = np.mean(Country_Populations_Array)
            print(f'Average population of {User_Country.name} over the past 20 years has been: {Avg_Num_of_Ppl:.2f}')

            #Population density in 2020:
            Ppl_Density_2020 = (pop_2020)/(User_Country.area)     
            print(f'Population density of the country in 2020 (most recent population density available): {Ppl_Density_2020:.2f} people per sq.km')

            
            #Population Growth year-on-year:
            Pop_Growth_list = [Country_Populations_List[i+1] - Country_Populations_List[i] for i in range(len(Country_Populations_List)-1)] #List comprehension that to get the population growth for each year
            Pop_Growth_Array = np.array(Pop_Growth_list)
            Max_Pop_Growth = np.max(Pop_Growth_Array)
            Max_Pop_Growth_Index = Pop_Growth_list.index(Max_Pop_Growth)
            if Max_Pop_Growth_Index <= 8:
                print(f'The year with the highest growth in population was 200{Max_Pop_Growth_Index}-200{Max_Pop_Growth_Index+1}')

            elif Max_Pop_Growth_Index == 9:
                print(f'The year with the highest growth in population was 200{Max_Pop_Growth_Index}-20{Max_Pop_Growth_Index+1}')
            
            elif 20>Max_Pop_Growth_Index>9:
                print(f'The year with the highest growth in population was 20{Max_Pop_Growth_Index}-20{Max_Pop_Growth_Index+1}')

            else:
                print('Error')





        ##################################### POPULATION DATA FOR THE SUB-REGION: #############################################################
            print(f'################################ POPULATION DATA FOR THE SUB-REGION & REGION OF {User_Country.name}: #########################################\n')
            Year_Choice = input(f'Enter the year for which you would like to view population data for {User_Country.sub_region} and {User_Country.region} (2000-2020): ')

            #Checking if the year choice is valid:
            if is_year_Valid(Year_Choice) == False:
                continue

            else:
                pass

            print('\n')
            
            print(f'###### POPULATION DATA FOR THE SUB-REGION #######\n')
            print(f'The sub-region of {User_Country.name} is: {User_Country.sub_region}\n')
            print(f'Countries present in the sub-region {User_Country.sub_region} are:')

            #Getting the countries in the same sub-region as the selected country together in a list and their areas:
            Sub_Region_Countries_list = []
            Sub_Region_Areas_list = []

            for i in range(Num_of_Countries):
                if User_Country.sub_region == Country_Data['SubRegion'][i]:
                    Sub_Region_Countries_list.append(Country_Data['Country'][i])
                    Sub_Region_Areas_list.append(Country_Data['Area'][i])
            
            #Printing the name of the countries in the same subregion:
            for Country in range(len(Sub_Region_Countries_list)):
                print(Sub_Region_Countries_list[Country], end=' | ')
            
            print('\n')

            #Getting the populations of the countries in the sub-region:
            Sub_Region_Populations_list = []
            

            for i in range(len(Sub_Region_Countries_list)): #for loop to iterate through the names of the countries in the sub-region
                for j in range(Num_of_Countries):   #for loop to iterate through the names of all countries in the Population_Data array
                    if Sub_Region_Countries_list[i] == Population_Data['Country'][j]:
                        Sub_Region_Populations_list.append(Population_Data[f'{Year_Choice}_Pop'][j])

            #Dictionary to relate countries and populations in the same region:
            Sub_Region_Countries_Population_Dict = dict(zip(Sub_Region_Populations_list, Sub_Region_Countries_list))


            #Total population of the sub-region in the chosen year:
            print(f'The total population of the sub-region {User_Country.sub_region} is: {sum(Sub_Region_Populations_list)}')

            #Total area of the sub-region:
            print(f'The total area of the sub-region {User_Country.sub_region} is: {sum(Sub_Region_Areas_list)}')

            #Country in the sub_region in the chosen year with the highest population:
            Max_Pop_Sub_Region = max(Sub_Region_Populations_list)
            for i in range(len(Sub_Region_Populations_list)):
                if Max_Pop_Sub_Region == Sub_Region_Populations_list[i]:
                    Max_Pop_Sub_Region_Country = Sub_Region_Countries_Population_Dict[Sub_Region_Populations_list[i]]
            
            print(f'The country with the largest population in {User_Country.sub_region} is: {Max_Pop_Sub_Region_Country}')

            #Dictionary to relate country areas in the sub-region with their name:
            Sub_Region_Countries_Area_Dict = dict(zip(Sub_Region_Areas_list, Sub_Region_Countries_list))

            #Country with the largest area in the sub-region:
            Max_Area_Sub_Region = max(Sub_Region_Areas_list)
            for i in range(len(Sub_Region_Areas_list)):
                if Max_Area_Sub_Region == Sub_Region_Areas_list[i]:
                    Max_Area_Sub_Region_Country = Sub_Region_Countries_Area_Dict[Sub_Region_Areas_list[i]]
            
            print(f'The country with the largest area in {User_Country.sub_region} is: {Max_Area_Sub_Region_Country}')

    
            #A list with the population densities of all countries in the sub region
            Sub_Region_Pop_Density_list = [] 

            for i in range(len(Sub_Region_Populations_list)):
                Sub_Region_Pop_Density_list.append(Sub_Region_Populations_list[i]/Sub_Region_Areas_list[i])
            
            #Dictionary to relate Population density (in the chosen year) of countries in the sub-region to country names:
            Sub_Region_Countries_Pop_Density_Dict = dict(zip(Sub_Region_Pop_Density_list, Sub_Region_Countries_list))


            #Country with the highest population density in the sub-region in the given year is:
            Max_Pop_Density_Sub_Region = max(Sub_Region_Pop_Density_list)
            for i in range(len(Sub_Region_Pop_Density_list)):
                if Max_Pop_Density_Sub_Region == Sub_Region_Pop_Density_list[i]:
                    Max_Pop_Density_Sub_Region_Country = Sub_Region_Countries_Pop_Density_Dict[Sub_Region_Pop_Density_list[i]]

            print(f'The country with the highest population density in {User_Country.sub_region} is: {Max_Pop_Density_Sub_Region_Country}')

            #Mean Population density of the region:
            Sub_Region_Pop_Density_array = np.array(Sub_Region_Pop_Density_list)
            print(f'Mean population density of the sub-region is: {Sub_Region_Pop_Density_array.mean():.2f}')


            

            

            print('\n\n')





            

                    
        ############################################# POPULATION DATA FOR THE REGION: ##########################################################
            print(f'###### POPULATION DATA FOR THE REGION #######\n')
            print(f'The UN designated region of {User_Country.name} is: {User_Country.region}')
            print(f'Countries present in {User_Country.region} are:')
            #Getting a list of the countries and their areas in the required region:
            Region_Countries_list = []
            Region_Areas_list = []

            for i in range(Num_of_Countries):
                if User_Country.region == Country_Data['Region'][i]:
                    Region_Countries_list.append(Country_Data['Country'][i])
                    Region_Areas_list.append(Country_Data['Area'][i])
            
            #Printing the name of the countries in the same region:
            for Country in range(len(Region_Countries_list)):
                print(Region_Countries_list[Country], end=' | ')
            
            print('\n')

            #Getting the populations of the countries in the region:
            Region_Populations_list = []

            for i in range(len(Region_Countries_list)): #for loop to iterate through the names of the countries in the sub-region
                for j in range(Num_of_Countries):   #for loop to iterate through the names of all countries in the Population_Data array
                    if Region_Countries_list[i] == Population_Data['Country'][j]:
                        Region_Populations_list.append(Population_Data[f'{Year_Choice}_Pop'][j])

            #List to array:
            Region_Populations_array = np.array(Region_Populations_list)
            Region_Areas_array = np.array(Region_Areas_list)

            #Dictionary to relate countries and populations in the same region:
            Region_Countries_Population_Dict = dict(zip(Region_Populations_list, Region_Countries_list))


            #Total population of the sub-region in the chosen year:
            print(f'The total population of {User_Country.region} is: {np.sum(Region_Populations_array)}')

            #Total area of the sub-region:
            print(f'The total area of the region {User_Country.region} is: {np.sum(Region_Areas_array)}')


            #Country in the sub_region in the chosen year with the highest population:
            Max_Pop_Region = max(Region_Populations_list)
            for i in range(len(Region_Populations_list)):
                if Max_Pop_Region == Region_Populations_list[i]:
                    Max_Pop_Region_Country = Region_Countries_Population_Dict[Region_Populations_list[i]]
            
            print(f'The country with the largest population in {User_Country.region} is: {Max_Pop_Region_Country}')


            #Dictionary to relate country areas in the sub-region with their name:
            Region_Countries_Area_Dict = dict(zip(Region_Areas_list, Region_Countries_list))

            #Country with the largest area in the sub-region:
            Max_Area_Region = max(Region_Areas_list)
            for i in range(len(Region_Areas_list)):
                if Max_Area_Region == Region_Areas_list[i]:
                    Max_Area_Region_Country = Region_Countries_Area_Dict[Region_Areas_list[i]]
            
            print(f'The country with the largest area in {User_Country.region} is: {Max_Area_Region_Country}')

            #A list with the population densities of all countries in the sub region
            Region_Pop_Density_list = [] 

            for i in range(len(Region_Populations_list)):
                Region_Pop_Density_list.append(Region_Populations_list[i]/Region_Areas_list[i])
            
            #Dictionary to relate Population density (in the chosen year) of countries in the sub-region to country names:
            Region_Countries_Pop_Density_Dict = dict(zip(Region_Pop_Density_list, Region_Countries_list))


            #Country with the highest population density in the sub-region in the given year is:
            Max_Pop_Density_Region = max(Region_Pop_Density_list)
            for i in range(len(Region_Pop_Density_list)):
                if Max_Pop_Density_Region == Region_Pop_Density_list[i]:
                    Max_Pop_Density_Region_Country = Region_Countries_Pop_Density_Dict[Region_Pop_Density_list[i]]

            print(f'The country with the highest population density in {User_Country.region} is: {Max_Pop_Density_Region_Country}')

            #Mean Population density of the region:
            Region_Pop_Density_array = np.array(Region_Pop_Density_list)
            print(f'Mean population density of the region is: {Region_Pop_Density_array.mean():.2f}')

            

            ################################## PLOTS FOR THE POPULATION DATA: #########################################################
            

            #Plot of population over the past 20 years:
            Years_Label = [2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
            plt.plot(Years_Array, Country_Populations_Array, color = 'blue', label='Population')
            plt.xticks(Years_Array, Years_Label, rotation = 'horizontal', fontsize = 6)
            plt.xlabel('Year')
            plt.ylabel('Population of the country')
            plt.title(f'Population vs Time ({User_Country.name})')
            plt.gca().legend(loc='center left', bbox_to_anchor=(0.7, 0.5))
            plt.show()

            #Plot of population density over the past 20 years:
            Ppl_Density_years = np.array([(x/User_Country.area) for x in Country_Populations_List])
            plt.plot(Years_Array, Ppl_Density_years, color = 'green', label = 'Population Density')
            plt.xticks(Years_Array, Years_Label, rotation = 'horizontal', fontsize = 6)
            plt.xlabel('Year')
            plt.ylabel('Population density of the country')
            plt.title(f'Population density vs Time ({User_Country.name})')
            plt.gca().legend(loc='center left', bbox_to_anchor=(0.7, 0.5))
            plt.show()

            #Plot of population growth over the past 20 years:
            Pop_Growth_Labels = ['2001-02','2002-03','2003-04','2004-05','2005-06','2006-07','2007-08','2008-09','2009-10','2010-11','2011-12','2012-13','2013-14','2014-15','2015-16','2016-17','2017-18','2018-19','2019-20','2020-21']
            Num_list = list(range(20))
            Num_Array = np.array(Num_list)
            plt.plot(Num_Array, Pop_Growth_Array, color='red', label = 'Population growth')
            plt.xticks(Num_Array, Pop_Growth_Labels, rotation = 'horizontal', fontsize = 6)
            plt.xlabel('Year')
            plt.ylabel('Population growth')
            plt.title(f'Population growth vs Time ({User_Country.name})')
            plt.gca().legend(loc='center left', bbox_to_anchor=(0.7, 0.5))
            plt.show()
            print('\n\n')
            



        elif choice == 3:
        ########################################### THREATENED SPECIES DATA FOR THE COUNTRY: #######################################################
            print(F'############ Threatened Species data of {User_Country.name}: ################\n') 
            
            for k in range(Num_of_Countries):
                if User_Country.name == Threatened_Species_Data['Country'][k]:
                    Num_Of_Threatened_Plants = Threatened_Species_Data['Plants'][k]
                    Num_Of_Threatened_Fish = Threatened_Species_Data['Fish'][k]
                    Num_Of_Threatened_Birds = Threatened_Species_Data['Birds'][k]
                    Num_Of_Threatened_Mammals = Threatened_Species_Data['Mammals'][k]
                   
            #Number of threatened species:
            print(f'Number of threatened plants in {User_Country.name} is: {Num_Of_Threatened_Plants}')
            print(f'Number of threatened fish in {User_Country.name} is: {Num_Of_Threatened_Fish}')
            print(f'Number of threatened fish in {User_Country.name} is: {Num_Of_Threatened_Birds}')
            print(f'Number of threatened mammals in {User_Country.name} is: {Num_Of_Threatened_Mammals}')

            Threatened_Species_List = [Num_Of_Threatened_Plants, Num_Of_Threatened_Fish,Num_Of_Threatened_Birds, Num_Of_Threatened_Mammals]
            Threatened_Species_Array = np.array(Threatened_Species_List)

            #Total number of threatened species per sq. km:
            Threatened_Species_Density = (Threatened_Species_Array.sum())/User_Country.area
            print(f'On average threatened species per sq. km in {User_Country.name} are: {Threatened_Species_Density}')


            #Species that is most threatened in the country:
            Max_Threatened = max(Threatened_Species_List)
            Max_Threatened_index = Threatened_Species_List.index(Max_Threatened)
            if Max_Threatened_index == 0:
                print(f'The most threatened species in {User_Country.name} are: Plants')

            elif Max_Threatened_index == 1:
                print(f'The most threatened species in {User_Country.name} is: Fish')

            elif Max_Threatened_index == 2:
                print(f'The most threatened species in {User_Country.name} are: Birds')

            else:
                print(f'The most threatened species in {User_Country.name} are: Mammals')

            print('\n\n')

            
        
        ########################################## THREATENED SPECIES DATA FOR THE SUB-REGION: ###################################################
            print('####### THREATENED SPECIES DATA FOR THE SUB-REGION: #########\n')
            print(f'The sub-region of {User_Country.name} is: {User_Country.sub_region}\n')
            print(f'Countries present in the sub region {User_Country.sub_region} are:')

            #Getting the countries in the same sub-region as the selected country together in a list and their areas:
            Sub_Region_Countries_list = []
            Sub_Region_Areas_list = []

            for i in range(Num_of_Countries):
                if User_Country.sub_region == Country_Data['SubRegion'][i]:
                    Sub_Region_Countries_list.append(Country_Data['Country'][i])
                    Sub_Region_Areas_list.append(Country_Data['Area'][i])
            
            #Printing the name of the countries in the same subregion:
            for Country in range(len(Sub_Region_Countries_list)):
                print(Sub_Region_Countries_list[Country], end=' | ')
            
            print('\n')
            
            #Lists with the threatened species data:
            Sub_Region_Plants_List = []
            Sub_Region_Fish_List = []
            Sub_Region_Birds_List = []
            Sub_Region_Mammals_List = []
            Sub_Region_Total_Threatened_Species = []

            #Getting threatened Species Data for all countries in the sub-region:
            for i in range(len(Sub_Region_Countries_list)):
                for k in range(Num_of_Countries):
                    if Sub_Region_Countries_list[i] == Threatened_Species_Data['Country'][k]:
                        Sub_Region_Plants_List.append(Threatened_Species_Data['Plants'][k])
                        Sub_Region_Fish_List.append(Threatened_Species_Data['Fish'][k])
                        Sub_Region_Birds_List.append(Threatened_Species_Data['Birds'][k])
                        Sub_Region_Mammals_List.append(Threatened_Species_Data['Mammals'][k])
                        Sub_Region_Total_Threatened_Species.append(Threatened_Species_Data['Plants'][k] + Threatened_Species_Data['Fish'][k] + Threatened_Species_Data['Birds'][k] + Threatened_Species_Data['Mammals'][k])

            
            #Country with the most number of threatened species:
            Max_Threatened_Sub_Region = max(Sub_Region_Total_Threatened_Species)
            Max_Threatened_Sub_Region_Index = Sub_Region_Total_Threatened_Species.index(Max_Threatened_Sub_Region)

            print(f'The country with the most threatened species in the sub-region is: {Sub_Region_Countries_list[Max_Threatened_Sub_Region_Index]}')

            ###Getting a list with Threatened Species per sq. km in a list:
            Threatened_Density_Sub_Region_list = []
            for i in range(len(Sub_Region_Countries_list)):
                Threatened_Density_Sub_Region_list.append(Sub_Region_Total_Threatened_Species[i]/Sub_Region_Areas_list[i])
            

            Threatened_Species_Density_Sub_Region_Max = max(Threatened_Density_Sub_Region_list)
            Threatened_Species_Density_Sub_Region_Max_index = Threatened_Density_Sub_Region_list.index(Threatened_Species_Density_Sub_Region_Max)
            print(f'The country with the most threatened species per sq.km in the sub-region is: {Sub_Region_Countries_list[Threatened_Species_Density_Sub_Region_Max_index]}')


            ###Country with the most number of threatened plants per sq.km:

            #Getting a list with number of threatened plants per sq.km:
            Threatened_Plants_Density_Sub_Region_list = []
            for i in range(len(Sub_Region_Countries_list)):
                Threatened_Plants_Density_Sub_Region_list.append(Sub_Region_Plants_List[i]/Sub_Region_Areas_list[i])


            #Finding the max number of threatened plants per sq. km and finding which country has it:
            Threatened_Plants_Density_Sub_Region_Max = max(Threatened_Plants_Density_Sub_Region_list)
            Threatened_Plants_Density_Sub_Region_Max_index = Threatened_Plants_Density_Sub_Region_list.index(Threatened_Plants_Density_Sub_Region_Max)
            print(f'The country with the most threatened plants per sq.km in the sub-region is: {Sub_Region_Countries_list[Threatened_Plants_Density_Sub_Region_Max_index]}')



            ###Country with the most number of threatened birds per sq.km:

            #Getting a list with number of threatened birds per sq.km:
            Threatened_Birds_Density_Sub_Region_list = []
            for i in range(len(Sub_Region_Countries_list)):
                Threatened_Birds_Density_Sub_Region_list.append(Sub_Region_Birds_List[i]/Sub_Region_Areas_list[i])

            #Finding the max number of threatened birds per sq. km and finding which country has it:
            Threatened_Birds_Density_Sub_Region_Max = max(Threatened_Birds_Density_Sub_Region_list)
            Threatened_Birds_Density_Sub_Region_Max_index = Threatened_Birds_Density_Sub_Region_list.index(Threatened_Birds_Density_Sub_Region_Max)
            print(f'The country with the most threatened birds per sq.km in the sub-region is: {Sub_Region_Countries_list[Threatened_Birds_Density_Sub_Region_Max_index]}')



            ###Country with the most number of threatened mammals per sq. km:

            #Getting a list with number of threatened mammals per sq.km:
            Threatened_Mammals_Density_Sub_Region_list = []
            for i in range(len(Sub_Region_Countries_list)):
                Threatened_Mammals_Density_Sub_Region_list.append(Sub_Region_Mammals_List[i]/Sub_Region_Areas_list[i])
            
            #Finding the max number of threatened mammals per sq. km and finding which country has it:
            Threatened_Mammals_Density_Sub_Region_Max = max(Threatened_Mammals_Density_Sub_Region_list)
            Threatened_Mammals_Density_Sub_Region_Max_index = Threatened_Mammals_Density_Sub_Region_list.index(Threatened_Mammals_Density_Sub_Region_Max)
            print(f'The country with the most threatened mammals per sq.km in the sub-region is: {Sub_Region_Countries_list[Threatened_Mammals_Density_Sub_Region_Max_index]}')
            

            print('\n\n')


        ########################################## THREATENED SPECIES DATA FOR THE REGION: #######################################################
            print('####### THREATENED SPECIES DATA FOR THE REGION: #########\n')
            print(f'The region of {User_Country.name} is: {User_Country.region} \n')
            print(f'Countries present in the sub region {User_Country.region} are:')

            #Getting the countries in the same sub-region as the selected country together in a list and their areas:
            Region_Countries_list = []
            Region_Areas_list = []

            for i in range(Num_of_Countries):
                if User_Country.region == Country_Data['Region'][i]:
                    Region_Countries_list.append(Country_Data['Country'][i])
                    Region_Areas_list.append(Country_Data['Area'][i])
            
            #Printing the name of the countries in the same subregion:
            for Country in range(len(Region_Countries_list)):
                print(Region_Countries_list[Country], end=' | ')
            
            print('\n')
            
            #Lists with the threatened species data:
            Region_Plants_List = []
            Region_Fish_List = []
            Region_Birds_List = []
            Region_Mammals_List = []
            Region_Total_Threatened_Species = []

            #Getting threatened Species Data for all countries in the sub-region:
            for i in range(len(Region_Countries_list)):
                for k in range(Num_of_Countries):
                    if Region_Countries_list[i] == Threatened_Species_Data['Country'][k]:
                        Region_Plants_List.append(Threatened_Species_Data['Plants'][k])
                        Region_Fish_List.append(Threatened_Species_Data['Fish'][k])
                        Region_Birds_List.append(Threatened_Species_Data['Birds'][k])
                        Region_Mammals_List.append(Threatened_Species_Data['Mammals'][k])
                        Region_Total_Threatened_Species.append(Threatened_Species_Data['Plants'][k] + Threatened_Species_Data['Fish'][k] + Threatened_Species_Data['Birds'][k] + Threatened_Species_Data['Mammals'][k])
                        
            
            #Country with the most number of threatened species:
            Max_Threatened_Region = max(Region_Total_Threatened_Species)
            Max_Threatened_Region_Index = Region_Total_Threatened_Species.index(Max_Threatened_Region)

            print(f'The country with the most threatened species is: {Region_Countries_list[Max_Threatened_Region_Index]}')

            ###Getting a list with Threatened Species per sq. km in a list:
            Threatened_Density_Region_list = []
            for i in range(len(Region_Countries_list)):
                Threatened_Density_Region_list.append(Region_Total_Threatened_Species[i]/Region_Areas_list[i])
            

            Threatened_Species_Density_Region_Max = max(Threatened_Density_Region_list)
            Threatened_Species_Density_Region_Max_index = Threatened_Density_Region_list.index(Threatened_Species_Density_Region_Max)
            print(f'The country with the most threatened species per sq.km is: {Region_Countries_list[Threatened_Species_Density_Region_Max_index]}')


            ###Country with the most number of threatened plants per sq.km:

            #Getting a list with number of threatened plants per sq.km:
            Threatened_Plants_Density_Region_list = []
            for i in range(len(Region_Countries_list)):
                Threatened_Plants_Density_Region_list.append(Region_Plants_List[i]/Region_Areas_list[i])


            #Finding the max number of threatened plants per sq. km and finding which country has it:
            Threatened_Plants_Density_Region_Max = max(Threatened_Plants_Density_Region_list)
            Threatened_Plants_Density_Region_Max_index = Threatened_Plants_Density_Region_list.index(Threatened_Plants_Density_Region_Max)
            print(f'The country with the most threatened plants per sq.km is: {Region_Countries_list[Threatened_Plants_Density_Region_Max_index]}')



            ###Country with the most number of threatened birds per sq.km:

            #Getting a list with number of threatened birds per sq.km:
            Threatened_Birds_Density_Region_list = []
            for i in range(len(Region_Countries_list)):
                Threatened_Birds_Density_Region_list.append(Region_Birds_List[i]/Region_Areas_list[i])

            #Finding the max number of threatened birds per sq. km and finding which country has it:
            Threatened_Birds_Density_Region_Max = max(Threatened_Birds_Density_Region_list)
            Threatened_Birds_Density_Region_Max_index = Threatened_Birds_Density_Region_list.index(Threatened_Birds_Density_Region_Max)
            print(f'The country with the most threatened birds per sq.km is: {Region_Countries_list[Threatened_Birds_Density_Region_Max_index]}')



            ###Country with the most number of threatened mammals per sq. km:

            #Getting a list with number of threatened mammals per sq.km:
            Threatened_Mammals_Density_Region_list = []
            for i in range(len(Region_Countries_list)):
                Threatened_Mammals_Density_Region_list.append(Region_Mammals_List[i]/Region_Areas_list[i])
            
            #Finding the max number of threatened mammals per sq. km and finding which country has it:
            Threatened_Mammals_Density_Region_Max = max(Threatened_Mammals_Density_Region_list)
            Threatened_Mammals_Density_Region_Max_index = Threatened_Mammals_Density_Region_list.index(Threatened_Mammals_Density_Region_Max)
            print(f'The country with the most threatened mammals per sq.km is: {Region_Countries_list[Threatened_Mammals_Density_Region_Max_index]}')



        else:
            print('Please enter a valid option')
            continue
        
    
if __name__ == '__main__':
    main()
