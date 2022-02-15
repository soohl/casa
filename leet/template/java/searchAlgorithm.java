public class searchAlgorithm{
    public void sequential(){ //or linear search
        int[] array = {10,300,30,498,37,60};
        int target = 498;
        int l = array.length;
        boolean found = false;
        for (int i = 0; i<l; i++){
            System.out.print(array[i] + " ");
        }
        System.out.println("Target number is " + String.valueOf(target));
        for (int i = 0; i<l; i++){
            if (array[i] == target){
                found = true;
                System.out.println("Found at a position "+ String.valueOf(i));
                break;
            }   
        }
        if (!found)
            System.out.println("Could not find target number "+ String.valueOf(target));
    }
    
    public void binary(){
        int[] array = {10,32,56,97,157,256,564,842,1009}; //must be sorted
        int target = 60;
        boolean found = false;
        int low =0;
        int high = array.length-1;
        int mid = 0;
        int ans = 0;
        for (int i = 0; i<=high; i++){
            System.out.print(array[i] + " ");
        }
        System.out.println("Target number is " + String.valueOf(target));
        while (!found && low <= high){
            mid = (low+high)/2;
            if (array[mid] == target){
                ans = mid;
                found = true;
            }else if(target > array[mid]){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        if (found)
            System.out.println("Found at the position "+ String.valueOf(ans));
        else
            System.out.println("Could not find target number "+ String.valueOf(target));
    }
}
