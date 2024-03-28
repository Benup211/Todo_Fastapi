import {useState} from 'react';
import {Button, Input} from '@chakra-ui/react';

const AddTodo=()=>{
    const [todo, setTodo]=useState('');
    return(
        <div>
            <Input placeholder="Add Todo" />
            <Button>Add</Button>
        </div>
    );
}
export default AddTodo;