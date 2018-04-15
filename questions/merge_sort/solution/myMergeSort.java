// this is a recursive algorithm
// o(n *log n)
// divide and conquer technique
// requires temp array to merge which makes mergesort a poor choice esp for large data sets

public static void myMergeSort(int arr[], int first, int last){ // sorts arr from first to last index provided
	
	if (first < last){ // if this is true the array is longer than 1
		int middle = Math.floor((first + last)/2); 
		myMergeSort(arr, first, middle);
		myMergeSort(arr, middle + 1, last); // you need to +1 the second half do that you dont use the middle index twice
		merge(arr, first, middle, last);
	}
}

// we merge the two subarrays by copying the elements to a temp array
// two incidices point to the current elements of each subarray, pushing smaller element into temp array
public static void merge(int arr[], int first, int middle, int last){

	int[] tempArr = {}; // or can set to size (arr.length)
	int i = first;
	int k = first;
	int j = middle + 1;

	// as long as the subarrays arent empty
	while (i <= middle && j <= last){
		if (arr[i] <= arr[j]){ // copy left subarray
			tempArr[k++] = arr[i++]; 
		} else { // copy right subarray
			tempArr[k++] = arr[j++];
		}
	}

	// copy remaining into temp array
	while (i <= middle){ 
		tempArr[k++] = arr[i++];
	}

	// copy remaining into temp array
	while (j <= last){ 
		tempArr[k++] = arr[j++];
	}

	// copy back the temp array into the main array
	for (int l = first; l <= last; l++){
		arr[l] = tempArr[l];
	}

}