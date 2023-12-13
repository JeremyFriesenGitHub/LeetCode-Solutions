function expect(val) {
    return {
        toBe: function(diff) {
            if (val !== diff) {
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe: function(diff) {
            if (val === diff) {
                throw new Error("Equal");
            }
            return true;
        }
    };
}

// Usage
try {
    const result = expect(5);
    console.log(result.toBe(5)); // Output: true
    console.log(result.notToBe(5)); // Throws an "Equal" error
} catch (error) {
    console.error(error.message); // Output: Equal
}
