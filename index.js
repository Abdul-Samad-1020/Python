import jsonfile from "jsonfile";
import moment from "moment";
import simpleGit from "simple-git";
const path = "./data.json";
const data = moment().subtract(5,'d').format();

const data = {
    date: data,
};
jsonfile.writeFile(path, data, ()   => {
    simpleGit().add([path]).commit(date,['--date':date]);
} );
